A,K = map(int,input().split())
count = 0
increase = 0

if K == 0:
	print(2000000000000 -A)
else:
	while True:
		count+=1
		A += 1+K*A
		if A >= 2000000000000:
			break
	print(count)