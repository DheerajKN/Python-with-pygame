option='y'
while option=='y':
    print("Enter the number whose factorial to find")
    num=int(input())
    fac=1
    while(num!=1):
        fac=fac*num
        num=num-1
    print("Factorial is "+str(fac))
    print("Do you want to continue?(y/n)")
    option=input()
print('Thank you for using this programme')
