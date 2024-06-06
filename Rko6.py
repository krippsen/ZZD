library(tidyverse)
library(lubridate)

tab <- read.csv("catalog.csv")
#print(head(tab))
#rint(typeof(tab$date))
tabMonth <- tab
tab$date <- year(mdy(tab$date))
#print(head(tab))
tab2 <- tab %>% 
    group_by(date) %>% 
    summarise(total = n())

tab2$cumsum <- cumsum(tab2$total)
print(head(tab2))

#plot(tab2$date,tab2$cumsum, type="l")

tabMonth$date <- month(mdy(tabMonth$date))

tabMonth2 <- tabMonth %>%
    group_by(date) %>%
    summarise(avg = mean(n()))

plot(tabMonth2$date, tabMonth2$avg, type="l")

print(head(tabMonth2))