N = int(input())
A = list(map(int,input().split()))

answer = 0
a = True

while a:
	count = 0
	for i in range(N):
		if A[i] % 2 == 0:
			A[i] /= 2
			count += 1
	if count == N:
		answer += 1
	else:
		a = False
		break

print(answer)