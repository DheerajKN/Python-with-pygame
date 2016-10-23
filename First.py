def Multiply(x,y):
    z = x * y
    print("Answer: ",z)

def Divide(x,y):
    if y != 0:
    	z = x / y
    	print("Answer: ",z)
    else:
    	print("Division by 0 is not defined")

def Add(x,y):
    z = x + y
    print("Answer: ",z)

def Subtract(x,y):
    z = x - y
    print("Answer: ",z)

ch = "y"

while ch == "Y" or ch == "y":

    operation = input("What would you like to do?\n1.Add\n2.Subtract\n3.Multiply\n4.Divide ")
    
    if operation == "1":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        Add(x,y)    
    elif operation == "2":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        Subtract(x,y)
    elif operation == "3":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        Multiply(x,y)
    elif operation == "4":
        x = float(input("First number: "))
        y = float(input("Second number: "))
        Divide(x,y)
    else:
        print("Wrong Input")
    ch = input("Would you like to continue ? y/n") 
