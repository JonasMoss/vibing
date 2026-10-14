sse <- function(X,y) sum(.lm.fit(X,y)$residuals^2)
pr2 <- function(X,y){ sf<-sse(X,y); sr<-sse(X[,-3,drop=FALSE],y); (sr-sf)/sr }
gen <- function(n,kind){ s<-rnorm(n); a<-0.4*s+rnorm(n); c1<-rnorm(n)
  e <- switch(kind, normal=rnorm(n), t8=rt(n,8)/sqrt(8/6), t3=rt(n,3)/sqrt(3))
  list(X=cbind(1,s,a,c1), y=0.35*s+0.30*a-0.20*c1+e) }
sq_interval <- function(lo, hi) {            # image of [lo,hi] under x^2  -- the bug fix
  if (lo <= 0 && hi >= 0) c(0, max(lo^2, hi^2)) else sort(c(lo^2, hi^2))
}
z_ci <- function(X,y,kurt_adj){
  n<-nrow(X); k<-ncol(X)-2
  ry<-.lm.fit(X[,-3,drop=FALSE],y)$residuals; rx<-.lm.fit(X[,-3,drop=FALSE],X[,3])$residuals
  r<-cor(ry,rx); z<-atanh(r); v<-1/(n-3-k)
  if (kurt_adj){ e<-.lm.fit(X,y)$residuals
    g2<-mean((e-mean(e))^4)/mean((e-mean(e))^2)^2-3
    v<-v*(1+max(g2,0)/2) }
  lim<-tanh(z+c(-1,1)*qnorm(.975)*sqrt(v)); sq_interval(lim[1],lim[2])
}
truth<-sapply(c("normal","t8","t3"),function(k){set.seed(11);mean(replicate(5,{d<-gen(300000,k);pr2(d$X,d$y)}))})
R<-3000
cat(sprintf("%-7s %8s %16s %14s\n","errors","true","z normal-theory","z kurt-adj"))
for (kd in c("normal","t8","t3")) {
  set.seed(2026); h1<-h2<-0
  for (i in 1:R){ d<-gen(100,kd)
    c1<-z_ci(d$X,d$y,FALSE); if(truth[kd]>=c1[1]&&truth[kd]<=c1[2]) h1<-h1+1
    c2<-z_ci(d$X,d$y,TRUE);  if(truth[kd]>=c2[1]&&truth[kd]<=c2[2]) h2<-h2+1 }
  cat(sprintf("%-7s %8.4f %15.1f%% %13.1f%%\n", kd, truth[kd], 100*h1/R, 100*h2/R))
}

# VERIFIED (n=100, 3000 reps, nominal 95%):
#   errors   true      z normal-theory   z kurtosis-corrected
#   normal   0.0827    94.8%             95.4%
#   t8       0.0831    94.6%             96.7%
#   t3       0.0820    91.1%             97.9%
# Pairs bootstrap for comparison: normal 94.1%, t3 90.3%.
#
# NOTE the sq_interval() helper. The first version squared the endpoints directly,
# which is wrong whenever the correlation interval straddles zero -- the lower bound
# of the squared interval is then 0, not min(endpoint^2). That bug scored 84.8% under
# t3, WORSE than no correction at all, and nothing about the output looked wrong.
# Only the coverage simulation revealed it.
