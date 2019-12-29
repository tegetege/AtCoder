A,B,K = map(int,input().split())
if A <= K :
	K -= A
	A = 0
	B = B - K
	if B <= 0:
		B = 0
	print(A,' ',B)
else:
	A -= K
	print(A,' ',B)