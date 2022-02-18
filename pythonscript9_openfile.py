#! /usr/bin/env python3

myfile = "rominas.py"
file = open(myfile, "w") ### a for append w for write r for read
####for line in file:
    ####print(line)

movies = ["the matrix" , "lancheros picudis"]

for m in movies:
     file.write(m + "\n")
file.close
file = open(myfile, "r") ### Read Only
for line in file:
    print(line)