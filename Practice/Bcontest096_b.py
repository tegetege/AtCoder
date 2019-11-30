num = list(map(int,input().split()))
K = int(input())

for i in range(K):
	num.sort(reverse=True)
	num[0] *= 2
print(sum(num))