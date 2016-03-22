class Fraction:
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom
	
	def __str__(self):
		return str(self.num) + "/" + str(self.den)
		
	def __add__(self, other):
		newnum = self.num * other.den + self.den * other.num
		newden = self.den * other.den
		common = gcd(newnum, newden)
		return Fraction(newnum // common, newden // common)
		
	def __dq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		
		return firstnum == secondnum
		
def gcd(m, n):
	while m % n != 0:
		oldm = m
		oldn = n
		
		m = oldn
		n = oldm % oldn
	return n

#print(gcd(20,10))
	
	
	
myf = Fraction(3,5)
print(myf)

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print(f3)

x = Fraction(1,2)
y = Fraction(2,3)

print(x+y)
print(x == y)
