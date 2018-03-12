class Matrix(object):
	def __init__(self, matrix):
		from fractions import Fraction
		if  not all(all(isinstance(elem, Fraction) for elem in row) for row in matrix):
			matrix = [[Fraction(elem).limit_denominator() for elem in row] for row in matrix]
		self.matrix = matrix
		self.rows = len(self.matrix)
		self.columns = len(self.matrix[0])

	def __str__(self):
		width = self.max_length() + 3
		s = "\n".join(["".join([str(elem).rjust(width) for elem in row]) for row in self.matrix])
		return s

	def max_length(self):
		longest = len(str(self.matrix[0][0]))
		for i in range(self.rows):
			for j in range(self.columns):
				length = len(str(self.matrix[i][j]))
				longest = length if length > longest else longest
		return longest

	def get_elem(self, i ,j):
		return self.matrix[i][j]

	def set_elem(self, i, j, new_elem):
		self.matrix[i][j] = new_elem

	def __add__(self, other):
		return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])

	def __sub__(self, other):
		return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])

	def __mul__(self, other):
		result = []
		for i in range(self.rows):
			row = []
			for j in range(other.columns):
				cij = 0
				for k in range(self.columns):
					cij += self.matrix[i][k] * other.matrix[k][j]
				row.append(cij)
			result.append(row)
		return Matrix(result)

	def __rmul__(self, scalar):
		return Matrix([[scalar * self.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])

	def __pow__(self, power):
		result = Matrix.id(self.rows)
		for n in range(power):
			result *= self
		return result

	def transpose(self):
		self.matrix =  [[self.matrix[i][j] for i in range(self.rows)] for j in range(self.columns)]
		self.rows, self.columns = self.columns, self.rows


	@staticmethod
	def id(n):
		return Matrix([[1 if i==j else 0 for j in range(n)] for i in range(n)])

	"""
	swaps the ith and jth row of a square matrix
	"""
	def switch_rows(self, i, j):
		E = Matrix.id(self.rows)
		E.set_elem(i, i, 0)
		E.set_elem(j, j, 0)
		E.set_elem(i, j, 1)
		E.set_elem(j, i, 1)
		self.matrix = (E*self).matrix

	def switch_columns(self, i, j):
		E = Matrix.id(self.columns)
		E.set_elem(i, i, 0)
		E.set_elem(j, j, 0)
		E.set_elem(i, j, 1)
		E.set_elem(j, i, 1)
		self.matrix = (self*E).matrix

	"""
	multiplies the ith row by a scalar k
	"""
	def scale_row(self, i, k):
		E = Matrix.id(self.rows)
		E.set_elem(i, i, k)
		self.matrix = (E*self).matrix

	"""
	adds k times the jth row to the ith row
	by default k is set to 1
	"""
	def add_to_row(self, i, j, k=1):
		E = Matrix.id(self.rows)
		E.set_elem(i, j, k)
		self.matrix = (E*self).matrix

	def is_identity(self):
		identity = Matrix.id(self.rows)
		return all(all(int(self.matrix[i][j]) == identity.matrix[i][j] for j in range(self.columns)) for i in range(self.rows))

	"""
	inverts the matrix if the inverse exists
	"""
	def invert(self):
		copy = Matrix(self.matrix)
		result = Matrix.id(self.rows)
		for j in range(self.columns):

			pivot = copy.get_elem(j, j)
			if pivot == 0:
				for k in range(j, self.rows-1):
					copy.switch_rows(j, k+1)
					pivot = copy.get_elem(j, j)
					if pivot != 0:
						break
				else:
					print("The matrix is not invertible")
					exit(-1)

			copy.scale_row(j, 1.0/pivot)
			result.scale_row(j, 1.0/pivot)
			for i in range(self.rows):
				if i != j:
					target = copy.get_elem(i, j)	# target is the element in the matrix that we want to eleminate
					copy.add_to_row(i, j, -target)
					result.add_to_row(i, j, -target)

		if copy.is_identity():
			self.matrix = result.matrix
		else:
			print("The matrix is not invertible")		

	@staticmethod
	def differentiation_matrix(n):
		return Matrix([[j if i+1==j else 0 for j in range(n)] for i in range(n)])

	@staticmethod
	def integration_matrix(n):
		return Matrix([[1/i if i==j+1 else 0 for j in range(n)] for i in range(n+1)])

	"""
	the coefficients (nx1 and mx1 matrices) of the first and second polynomials
	"""
	@staticmethod
	def polynomial_product(self_coef, other_coef):
		copy = Matrix(self_coef.matrix)
		copy.transpose()
		self_coefs = self_coef.matrix[0]
		product_matrix = []
		start = 0
		for i in range(len(other_coef.matrix)):
			row = []
			for j in range(len(other_coef.matrix)):
				if j == start:
					row += self_coefs
				else:
					row.append(0)
			product_matrix.append(row)
			start += 1
		product = Matrix(product_matrix)
		product.transpose()