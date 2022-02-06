import sys

N = int(input())
if N % 2 == 0:
	print(int(N/2))
	sys.exit()
else:
	print(int(N/2)+1)
	sys.exit()