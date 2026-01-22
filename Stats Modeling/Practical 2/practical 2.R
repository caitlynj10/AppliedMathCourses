setwd("C:/Users/caitlyn jones/OneDrive/classes/math/statistical modelling/Practical 2")
Data <- read.table("Stackloss.txt", header = TRUE)
head(Data)
attach(Data)
plot(Data)
plot(Air,Stkloss)
plot(Temp,Stkloss)
plot(Acid,Stkloss)
plot(Data)
lm(Stkloss~Air)
Model1 <- lm(Stkloss~Air)
summary(Model1)
ModelFull <- lm(Stkloss~Air+Temp+Acid)
summary(ModelFull)

# Discussion Questions
# 1. Air and Temperature
# 2. The null hypothesis is rejected meaning there is 
#    a relationship between Air and Stkloss
# 3. From the fitted model, you can see that Air and
#    Temperature have a relationship to Stkloss. To 
#    reduce the loss of Ammonia, we can reduce the
#    amount of Air or Temperature.

