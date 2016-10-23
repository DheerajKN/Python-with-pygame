option='y'
while option=='y':
    print("Enter first number")
    num1=int(input())
    print("Enter second number")
    num2=int(input())
    print("Enter third number")
    num3=int(input())
    if(num1>=num2&num1>=num3):
        print(str(num1)+" is largest among these numbers")
    elif(num2>=num1&num2>=num3):
        print(str(num1)+" is largest among these numbers")
    else:
        print(str(num3)+" is largest among these numbers")
    print("Do you want to continue?(y/n)")
    option=input()
print('Thank you for using this programme')

