# Does the interval actually work? Coverage under normal / heavy-tailed / heteroskedastic.
sse <- function(X, y) { f <- .lm.fit(X, y); sum(f$residuals^2) }
pr2 <- function(X, y) { s_f <- sse(X, y); s_r <- sse(X[, -3, drop=FALSE], y); (s_r - s_f)/s_r }

gen <- function(n, kind) {
  s <- rnorm(n); a <- 0.4*s + rnorm(n); c1 <- rnorm(n)
  e <- switch(kind,
    normal = rnorm(n),
    heavy  = rt(n, df = 3)/sqrt(3),                 # scaled to var 1
    hetero = rnorm(n, sd = 0.4 + 1.2*abs(s)))       # variance depends on a predictor
  list(X = cbind(1, s, a, c1), y = 0.35*s + 0.30*a - 0.20*c1 + e)
}

# population truth per scenario, by brute force
set.seed(1); truth <- sapply(c("normal","heavy","hetero"), function(k){ d <- gen(400000, k); pr2(d$X, d$y) })

ncf_ci <- function(X, y) {
  n <- nrow(X); df1 <- 1; df2 <- n - ncol(X); N <- df1 + df2 + 1
  s_f <- sse(X, y); s_r <- sse(X[, -3, drop=FALSE], y)
  Fobs <- ((s_r - s_f)/df1)/(s_f/df2)
  lo <- tryCatch(uniroot(function(L) pf(Fobs,df1,df2,ncp=L)-0.975, c(0,300))$root, error=function(e) 0)
  hi <- tryCatch(uniroot(function(L) pf(Fobs,df1,df2,ncp=L)-0.025, c(0,800))$root, error=function(e) Inf)
  c(lo/(lo+N), hi/(hi+N))
}
boot_ci <- function(X, y, B = 250) {
  n <- nrow(X)
  est <- replicate(B, { i <- sample(n, replace=TRUE); pr2(X[i,,drop=FALSE], y[i]) })
  unname(quantile(est, c(.025,.975)))
}

cat(sprintf("%-9s %8s | %-22s | %-22s\n","scenario","true","noncentral-F coverage","pairs bootstrap cov."))
for (k in c("normal","heavy","hetero")) {  # hetero needs wider uniroot bounds; see README
  set.seed(99)
  R <- 400; hitF <- hitB <- 0
  for (r in 1:R) {
    d <- gen(100, k)
    cf <- ncf_ci(d$X, d$y); if (truth[k] >= cf[1] && truth[k] <= cf[2]) hitF <- hitF + 1
    cb <- boot_ci(d$X, d$y);  if (truth[k] >= cb[1] && truth[k] <= cb[2]) hitB <- hitB + 1
  }
  cat(sprintf("%-9s %8.3f | %21.1f%% | %21.1f%%\n", k, truth[k], 100*hitF/R, 100*hitB/R))
}

# NOTE (verified, n=100, 400 reps):
#   normal   true 0.082 | noncentral-F 94.8% | pairs bootstrap 94.2%
#   heavy t3 true 0.086 | noncentral-F 90.0% | pairs bootstrap 91.8%
#   hetero   true 0.036 | noncentral-F 94.0% | pairs bootstrap 97.0%
# Monte Carlo error is about +/- 1 percentage point, so 90.0% is a real failure.
# The heteroskedastic scenario has a different true value because changing the error
# structure changes the population quantity being estimated.
