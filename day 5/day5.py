#Bucles
#Challenge 5.1 (Dont user sum() and len())
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

sum = 0
cont = 0

for student_height in student_heights:
  sum += student_height
  cont += 1

print(sum/cont)

#Challenge 5.2 (Dont use max() and min())
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max = 0
min = 100

for student_score in student_scores:
  if student_score > max:
    max = student_score
  elif student_score < min:
    min = student_score

print(f"The highest score in the class is: {max}")
print(f"The lower score in the class is: {min}")

#Challenge 5.3
#Write your code below this row 👇
total = 0
for number in range(1,101):
  if number % 2 == 0:
    total += number

print(total)

#Write your code below this row 👇
total = 0
for number in range(2,101,2):
  total += number

print(total)

#Challenge 5.4
#Write your code below this row 👇
for n in range(1,101):
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)


#Final Challenge

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for n in range(0, nr_letters):
  password += letters[random.randint(0, len(letters))]
for n in range(0, nr_symbols):
  password += symbols[random.randint(0, len(symbols))]
for n in range(0, nr_numbers):
  password += numbers[random.randint(0, len(numbers))]

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")