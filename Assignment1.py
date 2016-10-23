def add(x, y):
   print(a,"+",b,"=", x+y);

def subtract(x, y):
   print(a,"-",b,"=", x-y);

def multiply(x, y):
   print(a,"+",b,"=", x*y);

def divide(x, y):
   print(a,"+",b,"=", x/y);
   
m = 'y'

while m == 'y' or m == 'Y':
  print("Calculator")
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")
  choice=input("Enter your Choice: ")

  if choice == '1':
      a=float(input('Enter value of a: '))
      b=float(input('Enter value of b: '))
      add(a,b)
      m=input('Do you want to restart the calculator: ')

  elif choice == '2':
      a=float(input('Enter value of a: '))
      b=float(input('Enter value of b: '))
      subtract(a,b)
      m=input('Do you want to restart the calculator: ')

  elif choice == '3':
      a=float(input('Enter value of a: '))
      b=float(input('Enter value of b: '))
      multiply(a,b)
      m=input('Do you want to restart the calculator: ')
      
  elif choice == '4':
      a=float(input('Enter value of a: '))
      b=float(input('Enter value of b: '))
      divide(a,b)
      m=input('Do you want to restart the calculator: ')

  else:
   print("Invalid input")
