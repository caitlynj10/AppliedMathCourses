setwd("C:/Users/caitlyn jones/OneDrive/classes/math/statistical modelling/Practical 4")
Data <- read.table("Stackloss.txt", header = TRUE)
head(Data)
attach(Data)
ModelFull <- lm(Stkloss~Air+Temp+Acid)
summary(ModelFull)
ModelRed <- lm(Stkloss~Temp)
anova(ModelRed,ModelFull)
# The p-value of the partial F test is very small,
# so at usual levels we reject the null hypothesis
# from ModelRed and prefer ModelFull
Model2 <-lm(Stkloss~Air+Acid)
summary(Model2)
# ModelFull is better based on R^2 adj --> larger R^2 adj
AIC(ModelRed)
AIC(Model2)
AIC(ModelFull)
# ModelFull is the best model --> lowest AIC
pred.R2 <- function(model){
  X <- model.matrix(model)
  H <- X%*%solve(t(X)%*%X)%*%t(X)
  h <- diag(H)
  PRESS <- sum((model$residuals/(1-h))^2)
  SST <- sum((model$model[,1]-mean(model$model[,1]))^2)
  
  Rp <- 1-PRESS/SST
  Rp
}
pred.R2(ModelFull)
pred.R2(ModelRed)
pred.R2(Model2)
#ModelFull is the best --> largest R^2
Model.best <- step(ModelFull)
summary(Model.best)
plot(Model.best)


