def hamming_dist(x: int, y: int):
	
	hw = 0
	xory = x^y
	
	while xory > 0:

		if(xory & 1) != 0:
			hw += 1
		xory >>= 1

	return hw

x1 = input("x1:")
x2 = input("x2:")
print("hamming_dist(weight):", hamming_dist(int(x1), int(x2)))

