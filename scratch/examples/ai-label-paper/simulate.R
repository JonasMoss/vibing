# Simulate the raw Prolific export for the fictional "AI label" paper.
# Everything is made up. The seed search makes the planted problems hold
# exactly (see KEY.md). Writes build/prolific_export_2026-09-14.csv and
# build/stats.json.
#
#   Rscript scratch/examples/ai-label-paper/simulate.R

suppressMessages(library(jsonlite))
here <- dirname(normalizePath(sub("--file=", "", grep("--file=", commandArgs(FALSE), value = TRUE))))
out_dir <- file.path(here, "build")
dir.create(out_dir, showWarnings = FALSE)

clip <- function(x) pmin(7, pmax(1, round(x)))
hexid <- function(n, k) replicate(n, paste(sample(c(0:9, letters[1:6]), k, TRUE), collapse = ""))
alnum <- function(n, k) replicate(n, paste(sample(c(0:9, LETTERS, letters), k, TRUE), collapse = ""))

simulate <- function(seed) {
  set.seed(seed)
  n1 <- 560; n2 <- 80; n <- n1 + n2
  wave <- rep(1:2, c(n1, n2))
  cond <- sample(rep(c("AI", "control"), length.out = n))
  product <- sample(rep(c("candle", "charger"), length.out = n))
  ai <- as.integer(cond == "AI"); hed <- as.integer(product == "candle")
  w <- ifelse(hed == 1, 1, 0.25)                      # the label matters more for the candle

  A <- 4.6 - 0.55 * ai * w + rnorm(n, 0, 1.1)          # perceived authenticity
  P <- 4.5 + 0.35 * (1 - hed) + 0.40 * (A - 4.6) - 0.20 * ai * w + rnorm(n, 0, 1.05)

  pi <- sapply(1:3, function(j) clip(P + rnorm(n, 0, 0.55)))
  au <- sapply(1:4, function(j) clip(A + rnorm(n, 0, 0.75)))
  # auth_3 ("The description feels artificial") is reverse-worded, and a weaker item.
  au[, 3] <- clip(8 - (4.6 + 0.4 * (A - 4.6) + rnorm(n, 0, 0.6)))

  dur <- round(rlnorm(n, log(420), 0.45))
  attn <- rep(3L, n)
  type <- sample(c("ok", "inattentive", "speeder", "bigwtp"), n, TRUE, c(0.855, 0.05, 0.08, 0.015))
  ina <- type == "inattentive"
  attn[ina] <- sample(c(1:2, 4:7), sum(ina), TRUE)
  pi[ina, ] <- sample(1:7, sum(ina) * 3, TRUE); au[ina, ] <- sample(1:7, sum(ina) * 4, TRUE)
  sp <- type == "speeder"
  dur[sp] <- sample(48:118, sum(sp), TRUE)
  sl <- sample(4:7, sum(sp), TRUE)                     # straight-liners
  pi[sp, ] <- sl; au[sp, ] <- sl
  attn[sp] <- ifelse(runif(sum(sp)) < 0.3, sample(c(1:2, 4:7), sum(sp), TRUE), 3L)

  base <- ifelse(hed == 1, log(14), log(19))
  wtp <- round(exp(base - 0.03 * ai + rnorm(n, 0, 0.45)), 0)
  big <- type == "bigwtp"
  wtp[big] <- sample(c(120, 150, 200, 250, 500, 999), sum(big), TRUE)

  manip <- ifelse(ai == 1,
                  sample(c("Yes, by AI", "No", "Not sure"), n, TRUE, c(0.74, 0.12, 0.14)),
                  sample(c("Yes, by AI", "No", "Not sure"), n, TRUE, c(0.21, 0.55, 0.24)))

  start <- ifelse(wave == 1,
                  as.numeric(as.POSIXct("2026-08-27 09:00:00", tz = "UTC")) + runif(n, 0, 5.5 * 86400),
                  as.numeric(as.POSIXct("2026-09-10 09:00:00", tz = "UTC")) + runif(n, 0, 3.5 * 86400))
  o <- order(start)
  d <- data.frame(
    ResponseId = paste0("R_", alnum(n, 15)),
    StartDate = format(as.POSIXct(start, origin = "1970-01-01", tz = "UTC"), "%Y-%m-%d %H:%M:%S"),
    EndDate = format(as.POSIXct(start + dur, origin = "1970-01-01", tz = "UTC"), "%Y-%m-%d %H:%M:%S"),
    Duration_sec = dur, Finished = 1L, PROLIFIC_PID = hexid(n, 24),
    cond = cond, product = product, manip_check = manip, attn_check = attn,
    pi_1 = pi[, 1], pi_2 = pi[, 2], pi_3 = pi[, 3],
    auth_1 = au[, 1], auth_2 = au[, 2], auth_3 = au[, 3], auth_4 = au[, 4],
    wtp_raw = as.character(wtp),
    age = pmin(78, pmax(18, round(rnorm(n, 38, 12)))),
    gender = sample(c("Woman", "Man", "Non-binary", "Prefer not to say"), n, TRUE, c(.49, .47, .03, .01)),
    stringsAsFactors = FALSE)[o, ]
  # Messy WTP text, as people type it.
  m <- sample(nrow(d), 40); d$wtp_raw[m] <- paste0("$", d$wtp_raw[m])
  m <- sample(setdiff(seq_len(nrow(d)), m), 12); d$wtp_raw[m] <- paste(d$wtp_raw[m], "dollars")
  m <- sample(nrow(d), 9); d$wtp_raw[m] <- ""
  rownames(d) <- NULL
  d
}

wtp_num <- function(x) suppressWarnings(as.numeric(gsub("[^0-9.]", "", x)))

prep <- function(d, script = TRUE, reverse = FALSE) {
  d$wtp <- wtp_num(d$wtp_raw)
  keep <- d$attn_check == 3
  if (script) keep <- keep & d$Duration_sec >= 120 & (is.na(d$wtp) | d$wtp <= 100)
  d <- d[keep, ]
  d$PI <- rowMeans(d[, c("pi_1", "pi_2", "pi_3")])
  a3 <- if (reverse) 8 - d$auth_3 else d$auth_3
  d$AUTH <- rowMeans(cbind(d$auth_1, d$auth_2, a3, d$auth_4))
  d$ai <- as.integer(d$cond == "AI"); d$hed <- as.integer(d$product == "candle")
  d
}

simple <- function(d, prod) {
  s <- d[d$product == prod, ]
  t <- t.test(PI ~ factor(cond, levels = c("AI", "control")), data = s, var.equal = TRUE)
  list(t = unname(t$statistic), df = unname(t$parameter), p = t$p.value,
       m_ai = mean(s$PI[s$ai == 1]), m_ctl = mean(s$PI[s$ai == 0]),
       sd_ai = sd(s$PI[s$ai == 1]), sd_ctl = sd(s$PI[s$ai == 0]),
       n_ai = sum(s$ai == 1), n_ctl = sum(s$ai == 0))
}
inter <- function(d) {
  f <- summary(lm(PI ~ ai * hed, data = d))$coefficients["ai:hed", ]
  list(b = unname(f[1]), t = unname(f[3]), p = unname(f[4]), df = nrow(d) - 4)
}
alpha <- function(x) { k <- ncol(x); v <- var(x); k / (k - 1) * (1 - sum(diag(v)) / sum(v)) }
mediation <- function(d, B) {
  s <- d[d$product == "candle", ]
  ind <- function(s) coef(lm(AUTH ~ ai, s))[2] * coef(lm(PI ~ AUTH + ai, s))[2]
  boots <- replicate(B, ind(s[sample(nrow(s), replace = TRUE), ]))
  list(indirect = unname(ind(s)), lo = unname(quantile(boots, .025)), hi = unname(quantile(boots, .975)))
}

cheap <- function(d) {
  early <- d[as.POSIXct(d$StartDate, tz = "UTC") < as.POSIXct("2026-09-03", tz = "UTC"), ]
  sets <- list(draft = prep(early, TRUE), full_script = prep(d, TRUE),
               full_prereg = prep(d, FALSE), draft_reversed = prep(early, TRUE, TRUE),
               full_script_reversed = prep(d, TRUE, TRUE))
  st <- lapply(names(sets), function(nm) {
    s <- sets[[nm]]
    items <- as.matrix(s[, c("auth_1", "auth_2", "auth_3", "auth_4")])
    if (grepl("reversed", nm)) items[, 3] <- 8 - items[, 3]
    list(n = nrow(s), hedonic = simple(s, "candle"), utilitarian = simple(s, "charger"),
         interaction = inter(s), alpha_auth = alpha(items),
         alpha_pi = alpha(as.matrix(s[, c("pi_1", "pi_2", "pi_3")])),
         wtp_hedonic_p = t.test(wtp ~ cond, data = s[s$product == "candle", ])$p.value,
         wtp_util_p = t.test(wtp ~ cond, data = s[s$product == "charger", ])$p.value)
  })
  names(st) <- names(sets)
  list(st = st, sets = sets)
}

checks <- function(st) with(st, c(
  draft_hed = draft$hedonic$p > .003 && draft$hedonic$p < .02,
  draft_util = draft$utilitarian$p > .2,
  draft_int = draft$interaction$p > .08,
  full_hed = full_script$hedonic$p < .045,
  full_int = full_script$interaction$p > .05,
  prereg_hed = full_prereg$hedonic$p > .06 && full_prereg$hedonic$p < .2,
  alpha_raw = draft$alpha_auth > .52 && draft$alpha_auth < .66,
  alpha_rev = draft_reversed$alpha_auth > .82))

args <- commandArgs(TRUE)
if (length(args) && args[1] == "diag") {
  r <- t(sapply(20261203:(20261203 + 199), function(seed) checks(cheap(simulate(seed))$st)))
  print(colMeans(r)); cat("all:", sum(apply(r, 1, all)), "of", nrow(r), "\n")
  quit(save = "no")
}

for (seed in 20261203:20271203) {
  d <- simulate(seed)
  cs <- cheap(d)
  if (!all(checks(cs$st))) next
  set.seed(1)
  med <- lapply(cs$sets[c("draft", "draft_reversed", "full_script", "full_script_reversed", "full_prereg")], mediation, B = 5000)
  if (!(med$draft$hi < 0)) next
  st <- cs$st
  for (nm in names(med)) st[[nm]]$mediation <- med[[nm]]
  cat("seed", seed, "\n")
  write.csv(d, file.path(out_dir, "prolific_export_2026-09-14.csv"), row.names = FALSE)
  write_json(c(list(seed = seed), st), file.path(out_dir, "stats.json"), auto_unbox = TRUE, digits = 6, pretty = TRUE)
  break
}
