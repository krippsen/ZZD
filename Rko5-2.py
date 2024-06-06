library(tidyverse)

tabulka <- read.csv("StudentsPerformance.csv")


#plot(tabulka$math.score, tabulka$reading.score)
par(mfrow=c(1,2))

cor1P=cor(tabulka$math.score, tabulka$writing.score)
cor1S=cor(tabulka$math.score, tabulka$writing.score,method = "spearman")
plot(tabulka$math.score, tabulka$reading.score,main = paste(cor1P,cor1S,sep= "\n"))
plot(tabulka$math.score, tabulka$writing.score)
# Vykreslení prvního grafu
#plot(tabulka$math.score, tabulka$writing.score)
#plot(tabulka$reading.score, tabulka$writing.score)