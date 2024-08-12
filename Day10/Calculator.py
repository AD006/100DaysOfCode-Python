# Calculator
# def add(n1, n2):
#   return n1 + n2
#     def multiply(m1, m2):
#       return m1 * m2
#         def divide(d1, d2):
#           return d1 / d2
#             def subtract(s1, s2):
#               return s1 - s2

def add(n1, n2):
  return n1 + n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def subtract(n1, n2):
  return n1 - n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# num1=float(input("What is the first number? \n"))
# num2=float(input("What is the second number? \n"))
# for symbol in operations:
#   print(symbol)
# operation_symbol=input("Pick an operation from the line above: ")

# print(operations[operation_symbol](num1,num2))
# answer=operations[operation_symbol](num1,num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")

def calculator():
  print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
  should_continue=True
  num1=float(input("What is the first number? \n"))

  while should_continue:
    for symbol in operations:
      print(symbol)
    operation_symbol=input("Pick an operation: ")
    num2=float(input("What is the next number? \n"))
    answer=operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")=="y":
      num1=answer
    else:
      should_continue=False
      calculator()

calculator()