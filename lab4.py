#!/usr/bin/python3
'''For this task, write a program that will print out the numbers 1 through 100, each on their own line; 
however, if the number is evenly divisible by 3, print "Fizz" instead of the number. 
If the number is evenly divisible by 5, print "Buzz" instead of the number. 
And if the number is evenly divisible by both 3 and 5, print "Fizz Buzz" instead of the number.'''
for num in range(1,101):
    if (num % 3 == 0) and (num % 5 == 0):
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)
