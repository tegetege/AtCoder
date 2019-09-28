import sys
N , M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort(reverse=True)
for _ in range(M):
	A[0] = int(A[0] / 2)
	A.sort(reverse=True)

print(sum(A))