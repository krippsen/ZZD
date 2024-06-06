library(rvest)

Fibonacci <- function(n) {
  if (n <= 0) {
  } else if (n == 1) {
    return(c(0))
  } else if (n == 2) {
    return(c(0, 1))
  } else {
    fib <- numeric(n)
    fib[1] <- 0
    fib[2] <- 1
    
    for (i in 3:n) {
      fib[i] <- fib[i - 1] + fib[i - 2]
    }
    
    return(fib)
  }
}
print(Fibonacci(10))

Kvadraticka <- function(a,b,c){
D <- ((b^2.0) - (4*a*c))
if (D < 0){
    sprintf("Nemá řešení")
} else if (D > 0){
    x1 <- (-b+sqrt(D))/(a*2.0)
    x2 <- (-b-sqrt(D))/(a*2.0)
  sprintf("x1 = %-10f", x1)
  sprintf("x2 = %-10f", x2)
} else {
    x <- (-b/a*2.0)
    sprintf("x = %-10f", )
}
}


print(Kvadraticka(1,20,1))





df <- readRDS("tabulka.rds")
head(df,2)
print(df)