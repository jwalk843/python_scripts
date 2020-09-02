#!/usr/bin/python3

quote = "We'll not risk another frontal assault. That rabbit's dynamite."

print(len(quote))
print(quote.upper())
print(quote.replace("another", "a"))
print(quote[0:39])
print(len(quote[0:39].split()))
print(quote.split(".")[0] + ".")
print(quote[::-1])


#Print the length of the quote in characters
#Print the quote in all uppercase letters
#Print the sentence with the word "another" replaced with "a"
#Print the first sentence of the quote (don't forget the period!)
#Print the number of words in the first sentence
#Print the quote in reverse
print(quote.index)