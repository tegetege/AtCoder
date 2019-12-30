S = list(input())
N = int(input())

target = list()
for i in range(len(S)):
	for j in range(len(S)):
		target.append(S[i]+S[j])
print(target[N-1])