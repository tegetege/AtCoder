A,B,C,D = map(int,input().split())

def judge(ans):
	if ans > 0:
		print(ans)
	else:
		print(0)

if A < C :
	if B < D: 
		judge(B-C)
	else: 
		judge(D-C)
else:
	if B > D:
		judge(D-A)
	else:
		judge(B-A)

