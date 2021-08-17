def hamming_weight(n: int) -> int:
	
	#returns number of '1' in bits
	# in assumption that binary string length == 32
	# mask = 1 = 0000...0001 (31:0, 1:1) n & mask = defines if bit = 1 or 0
	# move '1' bit of mask by shifting to the left: 0000...0010
	# repeat

	bits: int = 0
	mask: int = 1 # 

	border = 32
	for i in range(border+1):
		if (n & mask) != 0:
			bits += 1
		mask <<= 1
	return bits
	
