setwd("C:/Users/caitlyn jones/OneDrive/classes/math/statistical modelling/Practical 3")
Data <- read.table("Stackloss.txt", header = TRUE)
head(Data)
attach(Data)
ModelFull <- lm(Stkloss ~ Air+Temp+Acid)
summary(ModelFull)
#finding a 95% CI for Air
beta <- ModelFull$coefficients
beta_sd <- summary(ModelFull)$coefficients[,2]
lower <- beta[2]-qt(0.975,17)*beta_sd[2]
upper <- beta[2]+qt(0.975,17)*beta_sd[2]
cbind(lower,upper)
confint(ModelFull)
predict(ModelFull)
#can also fo ModelFull$fitted.values
New.Values <- data.frame(Air = 60, Temp = 20, Acid = 59)
predict(ModelFull, New.Values)
New.Values2 <- data.frame(Air = c(60,65), Temp = c(20,15), Acid = c(59,59))
predict(ModelFull, New.Values2)
predict(ModelFull, New.Values2, se.fit = T)
predict(ModelFull, New.Values2, interval = "confidence")
predict(ModelFull, New.Values2, interval = "prediction")
predict(ModelFull, New.Values2, interval = "prediction", level = 0.99)
#ANOVA Tables
summary(ModelFull)
anova(ModelFull)
ModelNull <- lm(Stkloss~1)
anova(ModelNull, ModelFull)
# Discussion Questions
# 1. Res Df = Degrees of Freedom; RSS = sum of squares, with SSe = 1.7883 and 
#    Sst= 20.5924; Df = 3; Sum of Sq = SSr = 20.6924 - 1.7883; F = 59.902;
#    P value = 3.016e-09
# 2. The p value at the global F test is very small, so we can reject the
#    null hypothesis everywhere.
summary(ModelFull)
# R^2 = 0.9136 = 91.36% --> good model





