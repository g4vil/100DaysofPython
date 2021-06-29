#!/bin/python

#print()
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#\n
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

#string 
print("Hello " + "Gabriel")
print("Hello" + " Gabriel")
print("Hello" + " " + "Gabriel")
print("Hello","Gabriel")
print("Hello","Gabriel", sep=" ")

#String Manipulation
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#input
print("Whats yout name?")
#input("What is your name?")
name = input("Whats your name?")
print("Hello " + name)

#len
name = input("What is your name? ")
print(len(name))

print(len(input("What is your name? ")))

#little project Band Name Generator
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be "+ city + " " + pet + "\n\n")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/