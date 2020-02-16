N = int(input())

target = dict()
max_count = 0
max_key = list()
for i in range(N):
	S = str(input())
	if S in target:
		count = target[S] +1
		target[S] = count	
	else:
		target[S] = 1
		count = 1

	if max_count < count:
		max_count = count
		max_key = [S]
	elif max_count == count:
		max_key.append(S)

max_key.sort()
for i in max_key:
	print(i)