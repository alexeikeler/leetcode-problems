import math
#return what?

counter = 0

def bit_sum(num: int):
	
	# summ of bits in given number

	summ: int = 0
	
	#bit_string: str = ""
	
	print("given number (base 10): ", num)
	
	while num >= 1:
		
		if num % 2 == 1:
			summ += 1

		num //= 2

	#print("bit string: ", bit_string[::-1])

	#for i in range(len(bit_string)):
	#	summ += int(bit_string[i])

	print("binary sum: ", summ)

	sieve(summ) 


def sieve(num: int) -> None:
	
	#searching for prime


	A = [True for i in range(num+1)]
	A[0] = False
	A[1] = False
	
	for i in range(2, int(math.sqrt(num))+1):
		if A[i]:
			c=0
			while i**2 + (c*i) <= num:
				A[i**2 + (c*i)] = False
				c += 1
	
	for i in range(len(A)):
		if A[i] and i == num:
			global counter
			counter += 1



def solution(left: int, right: int) -> int:
	
	for i in range(left, right+1):
		bit_sum(i)


solution(10, 15)
print("total amount: ", counter)