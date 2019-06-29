N, K= map(int, input().split())

BB = N
RB = N-K

count = 0
for i in range(K-1):
	print(i)
	bunsi  = 1
	bunbo = 1
	for j in range(N-K+1,-1):
		bunsi  = bunsi * j
	print(bunsi)
	for j in range(i):
		bunbo  = bunbo * i 
	print(bunbo)