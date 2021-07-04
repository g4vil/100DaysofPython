#!/bin/python
#data types

#String
"Hello"
print("Hello"[0]) #print H
print("123"+"456")

#Integer (number without decimals)
print(123+456)
123456789
123_456_789

#Float
3.1416

#Boolean
True
False

#type()
num_char = len(input("What's your name?"))
new_num_char = str(num_char)
print("Your name has "+new_num_char+" characters.")
type(num_char)

str(), int(), float()

#2.1 Code Challenge
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Aritmetic
3 + 5
7 - 4
3 * 2
6 / 3 #return a float
4 ** 2 
4 % 2 #return rest
3 // 2 #return integer

#PEMDAS LR
#Parentesis ()
#Exponentes **
#Multiplicacion * Division /
#Adicion + Substracion -

print(3*3/3+3-3)

#Challenge 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)

print(int(new_weight/(new_height**2)))

#Redondeo
print(round(3/2))
print(3//2)
print(round(3/2, 2)) #Numero de decimales despues del punto.
print(f"Your score is {score}")

#Challenge time left
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rest = 90 - int(age)
days = rest * 365
weeks = rest * 52
months = rest * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left")

#Challenge TIp Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $ "))
porcentage = int(input("What percentange tip would you like to give? 10, 12, or 15? "))
number_of_persons = int(input("How many people to split the bill? "))

tip = total_bill * (porcentage/100)
total_bill += tip

total_individual = round(total_bill/number_of_persons,2)
print(f"Each person should pay: $ {total_individual}")
