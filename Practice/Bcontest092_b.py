N = int(input())
D,X = map(int,input().split())
A = list()
for i in range(N):
	A.append(int(input()))

chocolate = list()

for i in range(N):
	# print(i+1,'人目')
	choco_count = 0
	for j in range(1,D+1):
		day_count = 1 + A[i]*(j-1) 
		if day_count <= D:
			choco_count += 1 
		else:
			break
	# print('choco_count:',choco_count)
	chocolate.append(choco_count)
print(sum(chocolate)+X)