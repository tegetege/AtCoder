A,B = map(int,input().split())
if (abs(A-B)/2) % 1 != 0:
	print('IMPOSSIBLE')
else:
	print(int(min(A,B)+abs(A-B)/2))