class Fraction():
	def __init__(self, a=1, b=1):
		self.a = a
		self.b = b
		self.i = a / b

	def __str__(self):
		return str(self.a) + "/" + str(self.b)


	def __bool__(self):
		return bool(self.i)

	def __lt__(self, e):
		return (self.i < e.i)

	def __le__(self, e):
		return (self.i <= e.i)

	def __eq__(self, e):
		return (self.i == e.i)

	def __ne__(self, e):
		return (self.i != e.i)

	def __gt__(self, e):
		return (self.i > e.i)

	def __ge__(self, e):
		return (self.i >= e.i)


	def __add__(self, e):
		return Fraction(self.a * e.b + self.b * e.a, self.b * e.b)

	def __sub__(self, e):
		return Fraction(self.a * e.b - self.b * e.a, self.b * e.b)

	def __mul__(self, e):
		return Fraction(self.a * e.a, self.b * e.b)

	def __truediv__(self, e):
		return Fraction(self.a * e.b, self.b * e.a)

	def __floordiv__(self, e):
		return int(self / e)

	def __mod__(self, e):
		return self - Fraction(self // e) * e

	def __pow__(self, e):
		return self.i ** self.e


	def __neg__(self):
		return Fraction(-self.a, self.b)

	def __pos__(self):
		return Fraction(+self.a, self.b)

	def __abs__(self):
		if self.i > 0:
			return +self
		else:
			return -self


	def __int__(self):
		return int(self.i)

	def __float__(self):
		return float(self.i)


	def reduce(self):
		if self.b and not self.a:
			self.b = 0

		if not (self.a & 1 or self.b & 1):
			self.a /= 2
			self.b /= 2

		if not (self.a % 3 or self.b % 3):
			self.a /= 3
			self.b /= 3

		i = 6
		if abs(self.a) < abs(self.b):
			m = self.a
		else:
			m = self.b

		while i - 1 <= abs(m):
			if not (self.a % (i - 1) or self.b % (i - 1)):
				self.a /= i - 1
				self.b /= i - 1

			if not (self.a % (i + 1) or self.b % (i + 1)):
				self.a /= i + 1
				self.b /= i + 1

			i += 6

		return self

if __name__ == '__main__':
	a = Fraction(-85, 34)
	b = Fraction(1, 3)
	print(abs(-a.reduce()) % b)
