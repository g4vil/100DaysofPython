print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What'syour age? "))
    if age < 12:
        bill = 0
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("You got a free ride")
    else:
        bill = 12
        print("Adult tickets $12")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is: {bill}.")

else:
    print("Sorry, you have to grow taller before you can ride")



#Challenge 3.1
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (number % 2 == 0):
  print("This is an even number")
else:
  print("This is a odd number")

#Challenge 3.2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height**2), 1)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are slightly overweight")
elif bmi < 35:
    print("You are obesed")
else:
    print("You are clinically obese")

#Challenge 3.3
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else: 
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

#Chalenge 3.4
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
  bill = 15
elif size == "M":
  bill = 20
else:
  bill = 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: {bill}")

#Challenge 3.5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
true = 0
love = 0

for c in names:
  if c == "T" or c == "t":
    true += 1
  if c == "R" or c == "r":
    true += 1
  if c == "U" or c == "u":
    true += 1
  if c == "E" or c == "e":
    true += 1

for c in names:
  if c == "L" or c == "l":
    love += 1
  if c == "O" or c == "o":
    love += 1
  if c == "V" or c == "v":
    love += 1
  if c == "E" or c == "e":
    love += 1
  
n_true = str(true)
n_love = str(love)

pre_score = n_true + n_love
final_score = int(pre_score)


if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is: {final_score}")

#Challenge 3.5 Alternative solution
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



#final project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

one = input("left or right?")

if one == "left":
  two = input("swin or wait?")
  if two == "wait":
    three = input("which door?(pick a color)")
    if three == "red":
      print("You die burn")
    elif three == "blue":
      print("You are dinner for beast")
    elif three == "yellow":
      print("You Win")
    else:
      print("Game over")
  else:
    print("Atack by trough, game over!.")
else:
  print("Fall into a hole, Game Over!")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

