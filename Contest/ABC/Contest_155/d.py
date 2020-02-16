N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = list()
for i in range(N):
	for j in range(i+1,N):
		ans.append(A[i]*A[j])

ans.sort()
print(ans[K-1])