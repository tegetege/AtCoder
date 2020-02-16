import sys
N = int(input())
A = list(map(int,input().split()))

for i in range(len(A)):
	if A[i] % 2 == 0:
		# 偶数
		if A[i] % 3 == 0 or A[i] % 5 == 0:
			pass
		else:
			print('DENIED')
			sys.exit()

print('APPROVED')