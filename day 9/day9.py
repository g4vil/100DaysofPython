student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  if student_scores[key] >= 91:
    student_grades[key] = "Outstanding"
  elif student_scores[key] >= 81:
    student_grades[key] = "Exceeds Expetactions"
  elif student_scores[key] >= 71:
    student_grades[key] = "Acceptable"
  elif student_scores[key] <= 70:
    student_grades[key] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
  travel_log.append({"country":country, "visits":visits, "cities":cities})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Bienvenido a la subasta anonima")

participants = []

def get_info():
  answer = ""
  name = input("¿Cual es tu nombre? ")
  buck = int(input("¿Cuanto ofreces? $"))
  participants.append({"name":name,"buck":buck})
  
  answer = input("¿Va a participar alguien más? ")
  
  if answer == "yes":
    clear()
    get_info()
  if answer == "no":
    best_ofert = 0
    best_man = ""
    for participant in participants:
      if participant["buck"] > best_ofert:
        best_ofert = participant["buck"]
        best_man = participant["name"]
    
    print(f"The bes ofert was {best_ofert}, and the win was {best_man}")

get_info()


####Alternative solution
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()