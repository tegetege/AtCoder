S = list(input())
count = 0 
for i in range(len(S)):
	if S[i] == 'o':
		count += 100
print(700+count)