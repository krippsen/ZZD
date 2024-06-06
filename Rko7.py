library(tidyverse)
library(dplyr)
library(lubridate)
library(ggplot2)
tab <- read.csv("shootings.csv")

tab2 <- tab %>% group_by(state) %>% summarise(total = n()) %>% slice_max(order_by = total, n = 5)

#print(head(tab2,n = 5))

tab3 <- tab %>% 
  group_by(state, year=year(date)) %>%
  summarise(dead = n())

#barplot(tab3$year, tab3$dead)
#print(head(tab3))
tab4 <- tab

tab4$date <- ymd(tab4$date)
tab4$year <- year(tab4$date)


q <- tab4 %>% filter(state %in% tab2$state) %>% group_by(state, year) %>% count() %>%
    ggplot(aes(x=year, y=n, fill=state)) + geom_col() + facet_wrap(~state)

print(q)
q<-tab4 %>% group_by(armed) %>% count() %>% arrange(n) %>% head(10)
print(q)

