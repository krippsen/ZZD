
library(rvest)
tabulka <- read.csv("ZZD/StudentsPerformance.csv",sep=",")
tabulka["average_score"] <- round((tabulka$math.score + tabulka$reading.score + tabulka$writing.score) / 3, 2)
firstTen <- head(tabulka,10)

print(firstTen)
