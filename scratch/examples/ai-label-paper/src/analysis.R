# AI label study: analysis for draft v7
# KN, last edited 14 Sep 2026

d <- read.csv("data/prolific_export_2026-09-14.csv", stringsAsFactors = FALSE)
# d <- read.csv("data/prolific_export_2026-09-02.csv", stringsAsFactors = FALSE)  # first export

# WTP: people typed "$15", "15 dollars" etc.
d$wtp <- as.numeric(gsub("[^0-9.]", "", d$wtp_raw))

# Exclusions
d <- subset(d, attn_check == 3)                    # attention check (prereg)
d <- subset(d, Duration_sec >= 120)                # speeders (Ola, 9 Sep)
d <- subset(d, is.na(wtp) | wtp <= 100)            # silly WTP answers
nrow(d)

# Scales
d$PI   <- rowMeans(d[, c("pi_1", "pi_2", "pi_3")])
d$AUTH <- rowMeans(d[, c("auth_1", "auth_2", "auth_3", "auth_4")])

alpha <- function(x) { k <- ncol(x); v <- var(x); k / (k - 1) * (1 - sum(diag(v)) / sum(v)) }
alpha(as.matrix(d[, c("pi_1", "pi_2", "pi_3")]))
alpha(as.matrix(d[, c("auth_1", "auth_2", "auth_3", "auth_4")]))

# Sample
mean(d$age); sd(d$age); mean(d$gender == "Woman")

# Manipulation check
tab <- table(d$cond, d$manip_check == "Yes, by AI")
prop.table(tab, 1)
chisq.test(tab, correct = FALSE)

# Table 2
aggregate(cbind(PI, AUTH) ~ product + cond, data = d, FUN = function(x) c(m = mean(x), sd = sd(x), n = length(x)))

# H1/H2: effect of the label for each product
t.test(PI ~ cond, data = subset(d, product == "candle"), var.equal = TRUE)
t.test(PI ~ cond, data = subset(d, product == "charger"), var.equal = TRUE)

# H3: mediation for the candle, same as PROCESS model 4
c <- subset(d, product == "candle")
c$ai <- as.integer(c$cond == "AI")
a <- coef(lm(AUTH ~ ai, data = c))["ai"]
m <- lm(PI ~ AUTH + ai, data = c)
b <- coef(m)["AUTH"]
a * b
set.seed(2026)
boots <- replicate(5000, {
  r <- c[sample(nrow(c), replace = TRUE), ]
  coef(lm(AUTH ~ ai, data = r))["ai"] * coef(lm(PI ~ AUTH + ai, data = r))["AUTH"]
})
quantile(boots, c(.025, .975))
coef(m)["ai"]

# WTP (footnote)
t.test(wtp ~ cond, data = subset(d, product == "candle"), var.equal = TRUE)
