A,B,X = map(int,input().split())
if A <= X :
	print('YES') if (X - A) <= B else print('NO')
else:
	print('NO')