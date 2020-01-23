N = int(input())
S = list(input())
count = 0
for i in range(N):
	try:
		if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
			count += 1
	except IndexError:
		pass
print(count)