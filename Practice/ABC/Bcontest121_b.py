N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = list()
for i in range(N):
	a = list(map(int,input().split()))
	A.append(a)

count = 0
for i in range(N):
	ans = 0
	for j in range(M):
		ans += A[i][j]*B[j]
	if ans + C > 0:
		count += 1
print(count)