option='y'
while option=='y':
    print("Enter the number")
    num=int(input())
    if(num%2==0):
        print(str(num)+" is an even number")
    else:
        print(str(num)+" is a odd number")
    print("Do you want to continue?(y/n)")
    option=input()
print('Thank you for using this programme')
