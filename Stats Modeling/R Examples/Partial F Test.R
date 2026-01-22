library(MPV)
Delivery<-p8.3
x1<-Delivery$x1
x2<-Delivery$x2
y<-Delivery$y
fit.Del12<-lm(y~x1+x2, data=Delivery)
summary(fit.Del12)
anova(fit.Del12)
# SSe(B0,B1,B2) = 233.7
# SSr(B1|B0) = 5382.4
# SSr(B2|B0,B1) = 168.4
# SSr(B1,B2|B0) = 5382.4 + 168.4 = 5550.8
fit.Del21<-lm(y~x2+x1, data=Delivery)
anova(fit.Del21)
# SSr(B1,B2|B0) = 4599.1 + 951.7 = 5550.8
fit.Del1<-lm(y~x1, data=Delivery)
anova(fit.Del1, fit.Del12)
# SSe(B0,B1,B2) = 233.73
# SSe(B0,B1) = 402.13
# Partial F-Test = ((402.13-233.73)/1)/(233.73/22) = 15.851
fit.Del2<-lm(y~x2, data=Delivery)
anova(fit.Del2, fit.Del12)
fit.Del0<-lm(y~1, data=Delivery)
anova(fit.Del0, fit.Del12)