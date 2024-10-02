#!/usr/bin/python3

def read_file(filename=""):
    whit open(filename, "r", encoding="UFT-8") as file:
    print(file.read(), end="")
