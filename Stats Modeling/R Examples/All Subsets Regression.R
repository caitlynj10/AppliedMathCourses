library(leaps)
data(state)
statedata<-data.frame(state.x77)
tmp<-regsubsets(Life.Exp~., data=statedata,method="exhaustive")
summary(tmp)
summary(tmp)$adjr2
summary(tmp)$cp
summary(tmp)$bic
fit.main<-lm(Life.Exp~., data=statedata)
fit.by.step.aic<-step(fit.main,k=2)
tmp1<-regsubsets(Life.Exp~., data=statedata[-2,])
summary(tmp1)
library(MPV)
data<-p9.10
data$x4<-factor(data$x4,labels=c("Run1","Run2"))
str(data)
fit.by.allsubset<-regsubsets(y~x4*(x1+x2+x3+x5+x6),data=data,method="exhaustive",nvmax=11)
summary(fit.by.allsubset)
fit.asphalt.full<-lm(y~x4*(x1+x2+x3+x5+x6),data=data,)
step(fit.asphalt.full,k=2)
