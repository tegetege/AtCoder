X, A, B = map(int,input().split())

if B-A <= 0:
	print('delicious')
elif abs(A-B) <= X:
	print('safe')
else:
	print('dangerous')