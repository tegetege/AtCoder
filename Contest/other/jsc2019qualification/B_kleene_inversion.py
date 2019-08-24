import math

def cul_sum(count,K):
	ans = 0
	for i in range(K+1):
		ans += i
	print(ans)
	return ans

N,K = map(int,input().split())
A = list(map(int,input().split()))

count_ans = 0

for i in range(len(A)):
	count = 0
	for j in range(i+1,len(A)):
		if A[i] > A[j]:
			print(A[i],A[j])
			count+=1
	if count != 0:
		count_ans = cul_sum(count,K)

print(count_ans%(10**9+7))