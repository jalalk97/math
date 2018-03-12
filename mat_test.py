from mat import Matrix
 	
if __name__ == "__main__":
	a = [	[0,0,0,1,0,0,1],
		[0,0,0,1,0,1,0],
		[0,0,0,1,1,0,0],
		[1,1,1,1,1,1,1],
		[0,0,1,1,0,0,0],
		[0,1,0,1,0,0,0],
		[1,0,0,1,0,0,0]
	]
	A4 = Matrix(a)
	A4.switch_rows(0, 6)
	A4.switch_columns(0, 6)
	print(A4)
