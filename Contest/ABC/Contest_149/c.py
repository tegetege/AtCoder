import math
import sys

def judgement(num):
	dest = int(math.sqrt(num))
	for i in range(2,dest):
		if num % i == 0:
			return False
	return True
X = int(input())

while True:
	if judgement(X) == False:
		X += 1
	else:
		print(X)
		sys.exit()

