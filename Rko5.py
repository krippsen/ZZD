library(tidyverse)

tabulka <- read.csv("StudentsPerformance.csv")

avg <- mean(tabulka$math.score)
hodnoty <- 1:1000

#for(i in hodnoty)
#    hodnoty[i] <- abs(avg - mean(sample(tabulka$math.score, i)))

#plot(1:1000, hodnoty, type = "l")


vysledek <- sapply(hodnoty, function(x){ abs(avg - mean(sample(tabulka$math.score,x))) })

plot(vysledek,type = "l")