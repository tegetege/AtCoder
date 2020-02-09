N,M = map(int,input().split())
target = list()
for i in range(N):
	target.append(list(map(int,input().split())))

ans = target[0]
for i in range(1,len(target)):
	for j in range(target[i]):
		
