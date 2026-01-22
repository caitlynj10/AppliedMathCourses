setwd("C:/Users/caitlyn jones/OneDrive/classes/math/statistical modelling/Practical 5")
data("ToothGrowth")
attach(ToothGrowth)
sup.name<-unique(supp)
mean.effects<-c(mean(len[supp==sup.name[1]]),mean(len[supp==sup.name[2]]))
mean.effects
plot(c(-1,1),mean.effects,xaxt="n",type="b",
     xlab="Supplement type",ylab="Mean length",
     main="Mean effect of supplement type")
axis(2,at=c(15,16,17,18,20,21))
axis(1,at=c(-1,1),labels=sup.name)
dose.name<-unique(dose)
mean.effects<-c(mean(len[dose==dose.name[1]]),
                mean(len[dose==dose.name[2]]),
                mean(len[dose==dose.name[3]]))
mean.effects
plot(dose.name,mean.effects,type="b",xlab="dose",
     ylab="Mean length", main="Main effect of the dose")
interaction.plot(dose,supp,len)
# The dose has a positive effect on the response and 
# the supplement OJ has a positive effect with respect to
# VC supplement. However, the interaction between dose 
# and supplement is negative, with the difference
# between supplement types becoming negligible for larger doses value.
model_ANOVA<-lm(len~dose*supp)
summary(model_ANOVA)
Dose<-factor(dose)
model_TWO_WAY_ANOVA<-lm(len~Dose*supp)
summary(model_TWO_WAY_ANOVA)
is.factor(dose)
is.factor(Dose)
# Both model confirm the presence of significant effects 
# of the two factors and their interaction (notice
# that the value of the coefficient is positive because
# the reference level for the supplement is VC, i.e. the
# level with the smaller mean of the response).
set.seed(100)
x1<-c(-1,-0.5,0.5,1,-1,-0.5,0.5,1,0.3,-0.3,0.7,-0.7)
x2<-sample(x1,length(x1))
y<-(x1-0.5)^2+(x2+0.7)^2+x1*x2+rnorm(length(x1),0,0.1)
data<-data.frame(y,x1,x2)
plot(data)
model_opt<-lm(y~x1*x2+I(x1^2)+I(x2^2))
summary(model_opt)
beta<-model_opt$coefficients
b<-beta[2:3]
B<-matrix(0,2,2)
B[1,1]<-beta[4]
B[2,2]<-beta[5]
B[1,2]<-B[2,1]<-0.5*beta[6]
x_opt<--0.5*solve(B)%*%b
x_opt
eigen(B)$values 
range(x1)
range(x2)
# No, the point is outside of the range of 
# the observed variables for x1 and x2.

surg <- read.table("surgery.txt",header=T)
attach(surg)
head(surg)
plot(Age, surv)
surg1.glm <- glm(surv ~ Age, binomial, data=surg)
summary(surg1.glm)
step(surg1.glm)
plot(Age, surv, pch=20)
coefs = surg1.glm$coefficients
Ages = seq(from=49, to=73, length.out=1000)
g_mu = coefs[1] + Ages*coefs[2]
probs = exp(g_mu)/(1 + exp(g_mu)) 
points(Ages, probs, type="l")

