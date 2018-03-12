from polynomial import Polynomial
from mat import Matrix

if __name__ == "__main__":
	coef = Matrix([[1, 2, 1]])
	coef.transpose()
	f = Polynomial(coef)
	print(f*f)
	