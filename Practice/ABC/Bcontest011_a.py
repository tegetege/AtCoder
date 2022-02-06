import sys
N = int(input())
if N == 11:
	print(12)
	sys.exit()
print((N+1)%12)