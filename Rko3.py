library(rvest)
# získání html kodu
html_content <- read_html(url("https://ki.ujep.cz/cs/historie/"))
# nalezení všech tabulek na stránce, první řádek tabulek bude hlavička
list<- html_table(html_content, header = TRUE) # seznam tabulek
currList <- list[[2]]
changing <- subset(currList, subset = Do=="Dosud")
changing$Do <- "2024"
currList[currList$Do=="Dosud",] <- changing

currList$Do <- as.integer(currList$Do)
currList["celkem_let"] = currList$Do-currList$Od
currList<-currList[order(currList$celkem_let, decreasing = TRUE),]
print(currList)
