N = list(map(int,input()))
count = 1
for i in range(3):
	if N[i] == N[i+1]:
		count += 1
		if count == 3:
			break
	else:
		count = 1

print('Yes') if count >= 3 else print('No')