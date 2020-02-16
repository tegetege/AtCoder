N = list(map(int,input()))

count = 0
for i in range(len(N)):
	if N[i] <= 5:
		count += N[i]
	else:
		count += 1 + (10-N[i])
print(count)
