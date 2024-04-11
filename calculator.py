def begin():
  group = int(input("""welcome to the calculator what would you like to do?
  1. addition
  2. subtraction
  3. multiplication
  4. division  
  pick a number: """
  ))
  if group == 1:
    addition()
  elif group == 2:
    subtraction()
  elif group == 3:
    multiplication()
  elif group == 4:
    division()
  
    
    
  else:
    print("do it again except do it the right way")
    begin()
  
  

def addition():
  print("welcome to the addition calculator")
  num1 = int(input("enter the first number: "))
  num2 = int(input("enter the second number: "))
  sum = num1 + num2
  print("the sum of", num1, "and", num2, "is", sum)
  again = input("would you like to do another calculation? ")
  if again == "yes":
    begin()
  else:
    print("ok bye")
  



def subtraction():
  print("welcome to the subtraction calculator")
  num1 = int(input("enter the first number: "))
  num2 = int(input("enter the second number: "))
  dif = num1 - num2
  print(num1, "minus", num2, "is", dif)

def multiplication():
  print("welcome to the multiplication calculator")
  num1 = int(input("enter the first number: "))
  num2 = int(input("enter the second number: "))
  mult = num1 * num2
  print("the answer is", mult)
  again = input("would you like to do another calculation? ")
  if again == "yes":
    begin()
  else:
    print("ok bye")


def division():
  print("welcome to the division calculator")
  num1 = int(input("enter the first number: "))
  num2 = int(input("enter the second number: "))
  div = num1 / num2
  print("the answere is", div)
  
  again = input("would you like to do another calculation? ")
  if again == "yes":
    begin()
  else:
    print("ok bye")

begin()