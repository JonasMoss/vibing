# Reference implementation for the Day-2 demo: a confidence interval for partial R².
#
# You should NOT hand this to participants. The point of the block is that the agent
# writes this, live, from a sentence of English. This file exists so you can (a) check
# what it produces against something known, and (b) fall back if the room's wifi dies.
#
# Base R only — no packages, so it runs anywhere.
# Reproduces the numbers in README.md.  Run: Rscript partial-r2.R

set.seed(20260812)

# A survey-shaped study: job satisfaction from salary, autonomy, commute.
# Predictors are correlated, as they always are in real data.
make_data <- function(n, b_autonomy = 0.30) {
  salary   <- rnorm(n)
  autonomy <- 0.4 * salary + rnorm(n)
  commute  <- rnorm(n)
  y <- 0.35 * salary + b_autonomy * autonomy - 0.20 * commute + rnorm(n)
  data.frame(y, salary, autonomy, commute)
}

# Partial R² for `autonomy`: the share of the *remaining* variance it accounts for,
# once salary and commute have had their turn.
partial_r2 <- function(d) {
  full <- lm(y ~ salary + autonomy + commute, data = d)
  red  <- lm(y ~ salary + commute, data = d)
  sse_full <- sum(resid(full)^2)
  sse_red  <- sum(resid(red)^2)
  (sse_red - sse_full) / sse_red
}

# The interval nobody reports: resample the rows, refit, look at the spread.
#
# This is a NONPARAMETRIC PERCENTILE BOOTSTRAP with CASE resampling (rows, not
# residuals — the predictors are random here, it's survey data). It is the crudest
# option: percentile intervals are weakest exactly where partial R² lives, being
# bounded at 0, right-skewed and biased upward. Checked against the alternatives at
# n = 100 — BCa gives [0.022, 0.263] and the exact noncentral-F [0.024, 0.243],
# versus [0.024, 0.269] here, so the conclusion is robust to the choice. See README.
boot_ci <- function(d, B = 4000) {
  est <- replicate(B, partial_r2(d[sample(nrow(d), replace = TRUE), ]))
  quantile(est, c(0.025, 0.975))
}

# ---- the headline case -------------------------------------------------------
d    <- make_data(100)
full <- lm(y ~ salary + autonomy + commute, data = d)
pr2  <- partial_r2(d)
tval <- summary(full)$coefficients["autonomy", "t value"]
pval <- summary(full)$coefficients["autonomy", "Pr(>|t|)"]
ci   <- boot_ci(d)

cat(sprintf("partial R2 (autonomy) = %.3f   -> \"explains %.1f%% of the remaining variance\"\n",
            pr2, 100 * pr2))
cat(sprintf("t = %.2f, p = %.4f            -> comfortably significant\n", tval, pval))
cat(sprintf("bootstrap 95%% CI      = [%.3f, %.3f]  ->  [%.1f%%, %.1f%%]\n",
            ci[1], ci[2], 100 * ci[1], 100 * ci[2]))
cat(sprintf("the interval is %.1f times as wide as the estimate itself\n",
            (ci[2] - ci[1]) / pr2))

# ---- does more data rescue you? ---------------------------------------------
cat("\nmedian 95% CI width by sample size:\n")
for (n in c(50, 100, 200, 500, 1000)) {
  set.seed(n)
  reps <- replicate(40, {
    dd <- make_data(n)
    ci <- boot_ci(dd, B = 400)
    c(partial_r2(dd), ci[1], ci[2])
  })
  cat(sprintf("  n = %4d | partial R2 = %.3f | CI = [%.3f, %.3f] | width = %.3f\n",
              n, median(reps[1, ]), median(reps[2, ]), median(reps[3, ]),
              median(reps[3, ] - reps[2, ])))
}
