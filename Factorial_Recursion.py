option='y'
while option=='y':
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    print("Enter the number whose factorial to find")
    num=int(input())

    print(factorial(num))
    print("Do you want to continue?(y/n)")
    option=input()
print('Thank you for using this programme')
