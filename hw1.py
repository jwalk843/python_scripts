#!/usr/bin/python3

def getFib(n): 
      
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(f1, end = "\n") 
        next = f1 + f2 
        f1 = f2 
        f2 = next
          

getFib(10) 
  