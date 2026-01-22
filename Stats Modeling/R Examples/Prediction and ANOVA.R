data(cars)
x<-cars$speed
y<-cars$dist
plot(x,y, pch=19, cex = 0.6, xlab="Speed (mph)", ylab="Stopping distance (ft)" )
xmean<-mean(x)
ymean<-mean(y)
abline(v=xmean, h=ymean, lty=2)
mod<-lm(y~x)
summary(mod)
coef(mod)[2] + c(-1,1) * qt(0.975, df=48) * 0.4155
xnew <- c(12.5, 19.4)
predict(mod, newdata=data.frame(x=xnew), interval = "confidence")
predict(mod, newdata=data.frame(x=xnew), interval = "prediction")
anova(mod)