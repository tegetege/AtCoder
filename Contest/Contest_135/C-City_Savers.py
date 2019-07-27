N = int(input())
A = list(map(int,input().split()))
sum_A = sum(A)
B = list(map(int,input().split()))


for i in range(N):
	#Bが大きい場合
	if B[i]-A[i] >= 0:
		B[i] = B[i]-A[i]
		A[i] = 0
		if B[i]-A[i+1]>=0:
			A[i+1] = 0
			B[i] -=A[i+1]
		else:
			A[i+1] -= B[i]
	#Aが大きい場合
	else:
		A[i] -= B[i]


print(sum_A - sum(A))
