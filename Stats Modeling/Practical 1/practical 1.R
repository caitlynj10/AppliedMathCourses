setwd("C:/Users/caitlyn jones/OneDrive/classes/math/statistical modelling/Practical 1")
protein<-read.csv("protein.csv")
head(protein)
attach(protein)
mean(RedMeat)
mean(WhiteMeat)
mean(Eggs)
mean(Milk)
mean(Fish)
mean(Cereals)
mean(Starch)
mean(Nuts)
mean(Fr.Veg)
plot(RedMeat~Fish, col="lightblue",  main="Consumption of RedMeat and Fish", pch=19, cex=2, data=protein)
text(RedMeat~Fish, labels=Country, data=protein, cex=0.9, font=2)




