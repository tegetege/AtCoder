import sys

N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

if X <= Y:
	Z = list(range(X+1,Y+1))
else:
	print('War')
	sys.exit()

Z_x = max(x)+1
Z_y = min(y)
if Z_x <= Z_y:
	Z_xy = list(range(Z_x,Z_y+1))
else:
	print('War')
	sys.exit()

for i in Z_xy:
	if i in Z:
		print('No War')
		sys.exit()
print('War')
