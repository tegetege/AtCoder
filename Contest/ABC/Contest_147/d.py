N = int(input())
A = list(map(int,input().split()))

count = 0
for i in range(N):
	for j in range(i,N):
		count += A[i] ^ A[j]
print(count % (10 ** 9 +7))