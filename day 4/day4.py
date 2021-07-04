#challenge

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

result = random.randint(0,1)

if result == 0:
  print("Tails")
else:
  print("Heads")

#Challenge 2

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
who_pays = random.randint(0,len(names))

print(f"{names[who_pays]} is going to buy the meal today!")

#Challenge 2 Alternative Solution
import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

#Challenge
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0])-1 
row = int(position[1])-1

map[row][column] = 's'
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#Final Challenge Day 4
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the best game of the World Wide")

options = [rock, paper, scissors]
random_choice = random.randint(0, 2)
machine_choice = options[random_choice]
user_choice = int(input("Choice your weapon: \n1)Rock\n2)Paper\n3)Scissors\n"))

print(f"You select {options[user_choice-1]}\n")

print(f"The machine select {machine_choice}\n")

if (user_choice == 1 and random_choice == 1) or (user_choice == 2 and random_choice == 2) or (user_choice == 3 and random_choice == 0):
  print("The machine win!!!!!")
elif (user_choice == 1 and random_choice == 0) or (user_choice == 2 and random_choice == 1) or (user_choice == 3 and random_choice == 2):
  print("Its a tip")
else:
  print("You win")


#Final Challenge Solution
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")