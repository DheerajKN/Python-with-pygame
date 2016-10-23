option='y'
while option=='y':
   def recur_fibo(n):
      """Recursive function to
      print Fibonacci sequence"""
      if n <= 1:
          return n
      else:
          return(recur_fibo(n-1) + recur_fibo(n-2))


   # take input from the user
   nterms = int(input("How many terms? "))

   # check if the number of terms is valid
   if nterms <= 0:
      print("Please enter a positive integer")
   else:
      print("Fibonacci sequence:")
      for i in range(nterms):
          print(recur_fibo(i))
      print("Do you want to continue?(y/n)")
      option=input()
print('Thank you for using this programme')
