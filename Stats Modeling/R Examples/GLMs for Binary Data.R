age <- c(rep(1,5),rep(2,5),rep(3,5))
stage <- rep(c(1,2,3,4,5),3)
y<- c(11,15,2,5,18,3,3,5,0,1,4,4,3,3,2)
n <- c(12,16,4,18,19,4,7,8,25,3,5,12,15,93,5)
neuro<-data.frame(age=age, stage=stage, y=y,n=n)
neuro
neuro$agef <- factor(neuro$age)
neuro$stagef <- factor(neuro$stage)
str(neuro)
mod1 <- glm(cbind(y,n-y) ~ agef + stagef, family = binomial,data = neuro)
summary(mod1)
mod2 <- glm(cbind(y,n-y) ~ agef , family = binomial,data = neuro)
summary(mod2)
mod3 <- glm(cbind(y,n-y) ~ stagef, family = binomial,data = neuro)
summary(mod3)
mod_sa <- glm(cbind(y,n-y) ~ agef * stagef, family = binomial,data = neuro)
summary(mod_sa)
summary(mod1)$cov.unscale
beetle <- data.frame(dose=c(1.6907,1.7242,1.7552,1.7842,1.8113,
                            1.8369,1.8610,1.8839),
                     y=c(6,13,18,28,52,53,61,60),
                     n=c(59,60,62,56,63,59,62,60))
str(beetle)
model1 <- glm(cbind(y,n-y) ~ dose, family=binomial(link=logit),data=beetle)
summary(model1)
model2 <- glm(cbind(y,n-y) ~ dose, family=binomial(link=probit),data=beetle)
summary(model2)
model3 <- glm(cbind(y,n-y) ~ dose, family=binomial(link=cloglog),data=beetle)
summary(model3)
summary(model1)$aic
summary(model2)$aic
summary(model3)$aic
library(ISLR)
attach(Default)
head(Default)
logit_pred<-glm(default~balance+income+student,family="binomial",data=Default)
summary(logit_pred)
fitted_prob <- predict(logit_pred,type="response")
fitted_c <- ifelse(fitted_prob>0.5,"Yes","No")
table(Default$default,fitted_c)
105 / (228+105)
9627 / (9627+40)
fitted_c <- ifelse(fitted_prob>0.4,"Yes","No")
table(Default$default,fitted_c)
134 / (199+134)
9588 / (9588+79)
library(pROC)
ROC1 <- roc(Default$default,fitted_prob,plot=TRUE)
ROC1$auc
ind <- which.min((ROC1$sensitivities-1)**2+(ROC1$specificities-1)**2)
ROC1$thresholds[ind]
ROC1 <- roc(Default$default,fitted_prob,plot=TRUE)
points(ROC1$specificities[ind],ROC1$sensitivities[ind],pch=4,
       cex=3,col="red")
probit_pred<-glm(default~balance+income+student,
                 family="binomial"(link=probit),data=Default)
cloglog_pred<-glm(default~balance+income+student,
                  family="binomial"(link=cloglog),data=Default)
fitted_prob_probit <- predict(probit_pred,type="response")
fitted_prob_cloglog <- predict(cloglog_pred,type="response")
ROC2 <- roc(Default$default,fitted_prob_probit)
ROC3 <- roc(Default$default,fitted_prob_cloglog)
c(ROC1$auc,ROC2$auc,ROC3$auc)


