N = int(input())
H = list(map(int,input().split()))

max_count = 0
count = 0
try:
	for i in range(len(H)):
		if H[i] >= H[i+1]:
			# print(H[i],H[i+1],count+1)
			count += 1
		else:
			# print(H[i],H[i+1],0)
			max_count = max(max_count,count)
			count = 0
except:
	max_count = max(max_count,count)
print(max_count)