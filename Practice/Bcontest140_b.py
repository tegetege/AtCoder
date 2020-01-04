N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

count = 0
pre   = 0
for i in range(N):
	now = A[i] - 1
	count += B[now]
	if i != 0 and pre == now - 1:
		count += C[pre]
	pre = now
print(count)
