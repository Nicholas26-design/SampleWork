
### Basic packages to install before beginning ###


# Check to see if needed packages are installed
list.of.packages <- c("devtools", "stringr", "data.table", "tidyverse", "bit64", "lubridate","sqldf", "plyr","foreach","RODBC", "zoo", "XLConnect", "readxl", "openxlsx", "gdata",
                      "mailR", "RDCOMClient", "xlsx", "XML", "rJava", "RJDBC", "methods", "timeDate", "readxl", "writexl")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
install_github('omegahat/RDCOMClient')
if(length(new.packages)) install.packages(new.packages)

# require Packages
require("stringr")
require(data.table)
require(lubridate)
require(foreach)
require(RODBC)
require(mailR)
require(rJava)
require(RJDBC)
require(zoo)
require(XML)
require(methods)
require(XLConnect)
require(tidyverse)
require(readxl)
require(writexl)
require(openxlsx)
require(gdata)
require(timeDate)


# sql package
require(sqldf)
require(plyr)
require(devtools)


setwd()

# This will identify all  files in the folder
fileloop <- list.files(pattern="WEEKLY", full.names = TRUE)

# This pulls all  files in to create a dataframe 
ATB_df <- do.call("rbind.fill", lapply(fileloop, function(x) { 
  dat <- read.xlsx(x,sheet = 1,startRow = 1, colNames = TRUE)
  dat$fileName <- tools::file_path_sans_ext(basename(x))
  dat$filedate <- file.info(x)$ctime
  dat
}))

# Change class from char to date and makes a new variable

ATB_df$REPORT_DATE <- as.Date(BSHSIATB_df$REPORT_DATE, origin = '1899-12-30')


# Splits dataframe into List
SplitList <- split(ATB_df,ATB_df$fileName)


xlsxFileName1 <- paste("ATB_Week1",".xlsx",sep="") 
xlsxFileName2 <- paste("ATB_Week2",".xlsx",sep="") 
xlsxFileName3 <- paste("ATB_Week3",".xlsx",sep="")
xlsxFileName4 <- paste("ATB_Week4",".xlsx",sep="")


#Destination

setwd()

library(writexl)
write_xlsx(SplitList[[1]], xlsxFileName1)
write_xlsx(SplitList[[2]], xlsxFileName2)
write_xlsx(SplitList[[3]], xlsxFileName3)
write_xlsx(SplitList[[4]], xlsxFileName4)
