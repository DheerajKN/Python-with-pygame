option='y'
while option=='y':

   num = int(input("Display multiplication table of? "))

   # use for loop to iterate 10 times
   for i in range(1,11):
      print(num,'x',i,'=',num*i)
   print("Do you want to continue?(y/n)")
   option=input()
print('Thank you for using this programme')
