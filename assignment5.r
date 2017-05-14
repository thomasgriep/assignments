
mrate<-read.csv2("mrate.csv", sep=";")


str(mrate)

library(ggplot2)
library(tidyr)


p <- gather(mrate, Country, mortality, Netherlands:EU28)


ggplot(p, aes(x-year, y=mortality, color=Country)) + geom_line()


