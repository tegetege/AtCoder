import sys

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())

gap = [abs(a-e),abs(b-e),abs(c-e),abs(d-e)]

for i in range(len(gap)):
	if gap[i] > k:
		print(':(')
		sys.exit()
print('Yay!')
