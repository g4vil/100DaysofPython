#Write your code below this line 👇
import math

def paint_calc(height,width,cover):
  result = math.ceil((height*width)/cover)
  print(f"You'll need {result} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

##Challenge
#Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      is_prime = False
  
  if is_prime == True:
    print("Its a prime number.")
  else:
    print("Its no a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

##Challenge 1 Step
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text, shift):
  e_text = ""
  count = 0
  for c in "hello":
    for letter in alphabet:
      if c == letter:
        e_text += alphabet[count+shift]
      count += 1 
    count = 0
  
  print(f"The encode text is {e_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt("hello", 5)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text, shift):
  e_text = ""
  count = 0
  for c in text:
    for letter in alphabet:
      if c == letter:
        e_text += alphabet[count+shift]
      count += 1 
    count = 0
  
  print(f"The encode text is {e_text}")

def decrypt(text, shift):
  d_text = ""
  count = 0
  for c in text:
    for letter in alphabet:
      if c == letter:
        d_text += alphabet[count-shift]
      count += 1 
    count = 0
  
  print(f"The decode text is {d_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
while direction != "0":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)

###Final
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text, shift):
  e_text = ""
  count = 0
  for c in text:
    for letter in alphabet:
      if c == letter:
        e_text += alphabet[count+shift]
      count += 1 
    count = 0
  
  print(f"The encode text is {e_text}")

def decrypt(text, shift):
  d_text = ""
  count = 0
  for c in text:
    for letter in alphabet:
      if c == letter:
        d_text += alphabet[count-shift]
      count += 1 
    count = 0
  
  print(f"The decode text is {d_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while direction != "0":
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")