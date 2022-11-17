library(dplyr)
library(dbplyr)
library(DBI)


df = DBI::dbListTables(DB_JUR()) 
tbl(DB_JUR(), "jur_fallos")
tally(tbl(DB_JUR(), "jur_fallos"))


