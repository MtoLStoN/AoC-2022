#!/usr/bin/env Rscript
fileName=commandArgs(trailingOnly=TRUE)

string <- unlist(strsplit(readChar(fileName, file.info(fileName)$size),""))
l <- length(string)
for (i in 1:l) {
    if (length(unique(string[i:(i+3)])) == 4) {
        print(i+3)
        break
    }
}
for (i in 1:l) {
    if (length(unique(string[i:(i+13)])) == 14) {
        print(i+13)
        break
    }
}