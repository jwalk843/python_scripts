#!/usr/bin/python3
import sys
def find_the_Admiral(name):
    with open("admiralslist.txt", "r") as inputfile:
        if name in inputfile.read():
            return True
        else:
            return False
            
