library(faraway)
data(hsb)
str(hsb)
hsb$y <- as.factor(ifelse(hsb$prog == 'academic', 1 , 0))
fit1<- glm(y ~ gender + race + ses + schtyp + read + write + math
           + science + socst, family = binomial, data = hsb)
summary(fit1)
# First, consider stepwise search
drop1(fit1,test="LRT")
fit2 <- update(fit1, .~. - gender)
drop1(fit2,test = "LRT")
fit3 <- update(fit2, .~. - race)
drop1(fit3,test = "LRT")
fit4 <- update(fit3, .~. - write)
drop1(fit4,test = "LRT")
fit5 <- update(fit4, .~. - read)
drop1(fit5,test = "LRT")
fit6 <- update(fit5, .~. - ses)
drop1(fit6,test = "LRT")
anova(fit6,fit1,test="LRT")
# Stepwise search with BIC 1
n <- dim(hsb)[1]
step(fit1, k = log(n))
# Stepwise search with AIC 1
step(fit1, k = 2)
library(bestglm)
allsub_hsb <- hsb[,-c(1,6)]
head(allsub_hsb)
best.allsub.bic <- bestglm(allsub_hsb,IC = "BIC",family=binomial,method = "exhaustive")
summary(best.allsub.bic$BestModel)
best.allsub.aic <- bestglm(allsub_hsb,IC = "AIC",family=binomial,method = "exhaustive")
summary(best.allsub.aic$BestModel)
