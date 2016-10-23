import math
class Complex:
        
	def __init__(self, r=0, i=0):
		self.r = r
		self.i = i
		
	def __add__(self, n):
		return Complex(self.r + n.r, self.i + n.i)

	def __sub__(self, n):
		return Complex(self.r - n.r, self.i - n.i)

	def __mul__(self, n):
		real = (self.r*n.r - self.i*n.i)
		imag = (self.r*n.i + self.i*n.r)
		return Complex(real, imag)

	def __div__(self, n):
		real = (self.r*n.r + self.i*n.i)/(n.r**2 + n.i**2)
		imag = (self.i*n.r - self.r*n.i)/(n.r**2 + n.i**2)
		return Complex(real, imag)

	def __abs__(self):
		return (math.sqrt(self.r**2 + self.i**2))

	def __str__(self):

		if (self.i == 0):
			return ("%.2f" %(self.r))
		elif (self.r == 0):
			return ("%.2fi" %(self.i))
		else:
			if (self.i > 0):
				return ("%.2f + %.2fi" %(self.r, self.i))
			elif (self.i < 0):
				return ("%.2f - %.2fi" %(self.r, -1*self.i))

re_1 = float(input("Enter real part of first number : "))
img_1 = float(input("Enter imaginary part of first number : "))
re_2 = float(input("Enter real part of second number : "))
img_2 = float(input("Enter imaginary part of second number : "))

x = Complex(re_1, img_1)
y = Complex(re_2, img_2)

add = x + y
sub = x - y
mul = x * y
div = x.__div__(y)
modx = x.__abs__()
mody = y.__abs__()
print (add)
print (sub)
print (mul)
print (div)
print ("%.2f" %(modx))
print ("%.2f" %(mody))
