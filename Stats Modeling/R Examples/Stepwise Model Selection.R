data(state)
statedata<-data.frame(state.x77)
str(statedata)
round(cor(state.x77),3)
# Illiteracy, Murder, HS Grad have higher correlations
##Backward Elimination##
#removing every variable with signif. codes > 0.05
g<-lm(Life.Exp~., data=statedata)
drop1(g, test = "F")
# Remove Area
g1<-update(g, .~.-Area)
drop1(g1, test = "F")
# Remove Illiteracy
g2<-update(g1, .~.-Illiteracy)
drop1(g2, test = "F")
# Remove Income
g3<-update(g2, .~.-Income)
drop1(g3, test = "F")
# Remove Population
g4<-update(g3, .~.-Population)
drop1(g4, test = "F")
##Forward Selection##
#adding all variables with signig. codes < 0.05
f<-lm(Life.Exp~1, data=statedata)
add1(f, scope=g, test="F")
# Add Murder
f1<-update(f, .~. + Murder)
add1(f1, scope=g, test="F")
# Add HS Grad
f2<-update(f1, .~. + HS.Grad)
add1(f2, scope=g, test="F")
# Add Frost
f3<-update(f2, .~. + Frost)
add1(f3, scope=g, test="F")
##Stepwise Selection##
library(MPV)
data<-p9.10
data$x4<-factor(data$x4,labels=c("Run1", "Run2"))
str(data)
round(cor(p9.10),3)
fit1<-lm(y ~ x1+x2+x3+x4+x5+x6, data=data)
summary(fit1)
drop1(fit1, test= "F")
# Remove x6
fit2<-update(fit1, ~. -x6)
drop1(fit2, test="F")
# Remove x2
fit3<-update(fit2, ~. -x2)
drop1(fit3, test="F")
# Remove x5
fit4<-update(fit3, ~. -x5)
drop1(fit4, test="F")
# Remove x3
fit5<-update(fit4, ~. -x3)
drop1(fit5, test="F")
# Remove x1
fit6<-update(fit5, ~. -x1)
drop1(fit6, test="F")
fit7<-update(fit6, ~ .+x1+x1:x4)
anova(fit6,fit7)
summary(fit7)
fit8<-lm(y ~ x4*(x1+x2+x3+x5+x6),data=data)
drop1(fit8, test="F")
fit9<-update(fit8, ~ .-x4:x5)
drop1(fit9, test="F")
fit10<-update(fit9, ~ .-x4:x3)
drop1(fit10, test="F")
fit11<-update(fit10, ~ .-x3 -x5-x4:x6)
drop1(fit11, test="F")
fit12<-update(fit11, ~ .-x6)
drop1(fit12, test="F")
anova(fit12,fit8)
summary(fit8)$r.squared
summary(fit8)$adj.r.squared
summary(fit12)$r.squared
summary(fit12)$adj.r.squared




