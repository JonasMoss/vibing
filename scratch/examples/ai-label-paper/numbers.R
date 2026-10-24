# The numbers draft v7 quotes: the early export (before 3 September), the
# authors' exclusions, auth_3 not reversed. Also the numbers KEY.md needs.
#   Rscript scratch/examples/ai-label-paper/numbers.R
suppressMessages(library(jsonlite))
here <- dirname(normalizePath(sub("--file=", "", grep("--file=", commandArgs(FALSE), value = TRUE))))
d0 <- read.csv(file.path(here, "build", "prolific_export_2026-09-14.csv"), stringsAsFactors = FALSE)
wtp_num <- function(x) suppressWarnings(as.numeric(gsub("[^0-9.]", "", x)))
f2 <- function(x) formatC(x, format = "f", digits = 2)
pv <- function(p) if (p < .001) "< .001" else paste("=", sub("^0", "", formatC(p, format = "f", digits = 3)))
alpha <- function(x) { k <- ncol(x); v <- var(x); k / (k - 1) * (1 - sum(diag(v)) / sum(v)) }

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

report <- function(d, raw) {
  out <- list()
  out$n_raw <- nrow(raw)
  out$n_attn <- sum(raw$attn_check != 3)
  out$n_speed <- sum(raw$attn_check == 3 & raw$Duration_sec < 120)
  w <- wtp_num(raw$wtp_raw)
  out$n_wtp <- sum(raw$attn_check == 3 & raw$Duration_sec >= 120 & !is.na(w) & w > 100)
  out$n <- nrow(d)
  out$age_m <- f2(mean(d$age)); out$age_sd <- f2(sd(d$age))
  out$pct_women <- formatC(100 * mean(d$gender == "Woman"), format = "f", digits = 1)
  out$alpha_pi <- sub("^0", "", f2(alpha(as.matrix(d[, c("pi_1", "pi_2", "pi_3")]))))
  items <- as.matrix(d[, c("auth_1", "auth_2", "auth_3", "auth_4")])
  out$alpha_auth_raw <- sub("^0", "", f2(alpha(items)))
  items[, 3] <- 8 - items[, 3]
  out$alpha_auth_rev <- sub("^0", "", f2(alpha(items)))
  for (cell in list(c("AI", "candle"), c("control", "candle"), c("AI", "charger"), c("control", "charger"))) {
    s <- d[d$cond == cell[1] & d$product == cell[2], ]
    k <- paste(cell, collapse = "_")
    out[[paste0("n_", k)]] <- nrow(s)
    out[[paste0("pi_m_", k)]] <- f2(mean(s$PI)); out[[paste0("pi_sd_", k)]] <- f2(sd(s$PI))
    out[[paste0("auth_m_", k)]] <- f2(mean(s$AUTH)); out[[paste0("auth_sd_", k)]] <- f2(sd(s$AUTH))
    out[[paste0("wtp_m_", k)]] <- f2(mean(s$wtp, na.rm = TRUE)); out[[paste0("wtp_sd_", k)]] <- f2(sd(s$wtp, na.rm = TRUE))
  }
  for (prod in c("candle", "charger")) {
    s <- d[d$product == prod, ]
    t <- t.test(PI ~ factor(cond, levels = c("AI", "control")), data = s, var.equal = TRUE)
    sp <- sqrt(((sum(s$ai == 1) - 1) * var(s$PI[s$ai == 1]) + (sum(s$ai == 0) - 1) * var(s$PI[s$ai == 0])) / (nrow(s) - 2))
    out[[paste0("t_", prod)]] <- f2(t$statistic); out[[paste0("df_", prod)]] <- unname(t$parameter)
    out[[paste0("p_", prod)]] <- pv(t$p.value)
    out[[paste0("d_", prod)]] <- f2((mean(s$PI[s$ai == 1]) - mean(s$PI[s$ai == 0])) / sp)
    tw <- t.test(wtp ~ factor(cond, levels = c("AI", "control")), data = s, var.equal = TRUE)
    out[[paste0("wtp_t_", prod)]] <- f2(tw$statistic); out[[paste0("wtp_df_", prod)]] <- unname(tw$parameter)
    out[[paste0("wtp_p_", prod)]] <- pv(tw$p.value)
    ta <- t.test(AUTH ~ factor(cond, levels = c("AI", "control")), data = s, var.equal = TRUE)
    out[[paste0("auth_t_", prod)]] <- f2(ta$statistic); out[[paste0("auth_p_", prod)]] <- pv(ta$p.value)
    out[[paste0("auth_df_", prod)]] <- unname(ta$parameter)
  }
  f <- summary(lm(PI ~ ai * hed, data = d))$coefficients["ai:hed", ]
  out$int_b <- f2(f[1]); out$int_t <- f2(f[3]); out$int_p <- pv(f[4]); out$int_df <- nrow(d) - 4
  mc <- table(d$cond, d$manip_check == "Yes, by AI")
  out$manip_ai_pct <- formatC(100 * mc["AI", "TRUE"] / sum(mc["AI", ]), format = "f", digits = 1)
  out$manip_ctl_pct <- formatC(100 * mc["control", "TRUE"] / sum(mc["control", ]), format = "f", digits = 1)
  ch <- suppressWarnings(chisq.test(mc, correct = FALSE))
  out$manip_chi <- f2(ch$statistic); out$manip_p <- pv(ch$p.value)
  s <- d[d$product == "candle", ]
  a <- coef(lm(AUTH ~ ai, s))[2]; bm <- lm(PI ~ AUTH + ai, s); b <- coef(bm)[2]; cp <- coef(bm)[3]
  set.seed(2026)
  boots <- replicate(5000, { r <- s[sample(nrow(s), replace = TRUE), ]
    coef(lm(AUTH ~ ai, r))[2] * coef(lm(PI ~ AUTH + ai, r))[2] })
  out$med_a <- f2(a); out$med_b <- f2(b); out$med_cprime <- f2(cp)
  out$med_ind <- f2(a * b); out$med_lo <- f2(quantile(boots, .025)); out$med_hi <- f2(quantile(boots, .975))
  out
}

raw <- d0
early <- raw[as.POSIXct(raw$StartDate, tz = "UTC") < as.POSIXct("2026-09-03", tz = "UTC"), ]
res <- list(
  draft = report(prep(early), early),
  current_script = report(prep(raw), raw),
  current_prereg = report(prep(raw, script = FALSE, reverse = TRUE), raw))
write_json(res, file.path(here, "build", "numbers.json"), auto_unbox = TRUE, pretty = TRUE)
cat("ok\n")
