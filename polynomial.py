from mat import Matrix

class Polynomial(object):
	"""
	coefficients is a list that contins the coefficients of each power 
	of x in ascending order. An nx1 matrix may be supplied as well.
	"""
	def __init__(self, coefficients):
		self.coefficients = coefficients
		self.degree = self.coefficients.rows

	def __str__(self):
		return " + ".join(["{0}x^{1}".format(self.coefficients.matrix[i][0], i) for i in range(self.degree)])

	def __add__(self, other):
		return Polynomial(self.coefficients+other.coefficients)		

	def __sub__(self, other):
		return Polynomial(self.coefficients-other.coefficients)

	def __mul__(self, other):
		product_matrix = Matrix.polynomial_product(self.coefficients, other.coefficients)
		product = product_matrix * other
		return Polynomial(product)

	def __rmul__(self, scalar):
		return Polynomial(scalar * self.coefficients)

if __name__ == "__main__":
	coef = Matrix([[1, 2, 1]])
	coef.transpose()
	f = Polynomial(coef)
	print(f*f)
	
