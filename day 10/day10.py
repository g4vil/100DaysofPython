#Challenge 10.1
input_name = "Gabriel"
input_last = "Villegas"

def format_name(input_name, input_last):
  result = input_name + " " + input_last
  return result.title()

print(format_name("Gabriel","Villegas"))

#Challenge 10.2
def is_leap(year):
  """This is a Docstring Example"""  
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#Challenge 10.3
def add(a, b):
  """return the sum of a and b"""
  return a + b

def sub(a, b):
  """return the substract of a and b"""
  return a - b

def mul(a, b):
  """return the multiply of a and b"""
  return a * b

def div(a, b):
  """return the division of a and b"""
  return a / b

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
  }

input_a = int(input("Ingresa el primer numero: "))

for symbol in operations:
  print(symbol)

continuar = True

while continuar:
  selected_operation = input("Selecciona una operacion: ")
  input_b = int(input("Ingresa el siguiente numero: "))
  calcular = operations[selected_operation]
  answer = calcular(input_a, input_b)
  print(f"{input_a} {selected_operation} {input_b} = {answer}")

  if input(f"Escribe 'y' para continuar calculando con {answer}, o escribe 'n' para salir") == "y":
    input_a = answer
  else:
    continuar = False
    print("gracias, vuelve pronto")

  from art import logo

def add(a, b):
  """return the sum of a and b"""
  return a + b

def sub(a, b):
  """return the substract of a and b"""
  return a - b

def mul(a, b):
  """return the multiply of a and b"""
  return a * b

def div(a, b):
  """return the division of a and b"""
  return a / b

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
  }

def calculator():
  print(logo)
  input_a = float(input("Ingresa el primer numero: "))

  for symbol in operations:
    print(symbol)

  continuar = True

  while continuar:
    selected_operation = input("Selecciona una operacion: ")
    input_b = float(input("Ingresa el siguiente numero: "))
    calcular = operations[selected_operation]
    answer = calcular(input_a, input_b)
    print(f"{input_a} {selected_operation} {input_b} = {answer}")

    if input(f"Escribe 'y' para continuar calculando con {answer}, o escribe 'n' para salir ") == "y":
      input_a = answer
    else:
      continuar = False
      calculator()

calculator()