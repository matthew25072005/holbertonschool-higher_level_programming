#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = " ".join(str.split()[39:41]) + " " + " ".join(str.split()[2:5]) + " with " + str.split()[0]
print(str)
