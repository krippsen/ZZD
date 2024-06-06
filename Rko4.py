library(rvest)
library(ggplot2)
library(dplyr)
tabulka <- read.csv("ZZD/StudentsPerformance.csv",sep=",")
tabulka["average_score"] <- round((tabulka$math.score + tabulka$reading.score + tabulka$writing.score) / 3, 2)

#plot(tabulka$writing.score,tabulka$reading.score, asp=1, xlab="Writing Score", ylab="Reading Score")
#tabulka %>% ggplot(aes(x=writing.score,y=reading.score),color=Red) + geom_point()

#print(ggplot(tabulka,aes(tabulka$writing.score,tabulka$reading.score)) + geom_point())

#hist(tabulka$average_score , main="Průměrné skóre", 
     #xlab="Skore",ylab="Četnost", sub="Fig. 1: histogram průměrného skóre")

print(ggplot(tabulka,aes(tabulka$average_score)) + geom_histogram(bins = 10,color="red",fill="limegreen") + theme_classic())

#boxplot(tabulka$math.score~tabulka$race.ethnicity , main="Skore z matiky", xlab= "ethnikum",ylab="skore", 
        #sub="Fig. 1: Skore z matiky podle etnika")

tabulka$gender <- as.factor(tabulka$gender)
tabulka$race.ethnicity <- as.factor(tabulka$race.ethnicity)
#print(ggplot(tabulka,aes(y=math.score,fill=race.ethnicity)) +geom_boxplot() + 
  #facet_wrap(~tabulka$gender))
#print(ggplot(tabulka,aes(tabulka$math.score,fill=tabulka$gender)) + geom_boxplot())
