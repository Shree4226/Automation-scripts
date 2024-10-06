# Python program to check whether number is 
# refactorable or not 
import math 

def isRefactorableNumber(n): 

	# Initialize result 
	divCount = 0

	for i in range(1,int(math.sqrt(n))+1): 

		if n % i == 0: 

			# If divisors are equal, count only one 
			if n/i == i: 
				divCount += 1

			else: # Otherwise count both 
				divCount += 2

	return n % divCount == 0


# Driver Code 
n = 8
if isRefactorableNumber(n): 
	print ("yes") 
else: 
	print ("no") 

n = 14
if (isRefactorableNumber(n)): 
	print ("yes") 
else: 
	print ("no") 
