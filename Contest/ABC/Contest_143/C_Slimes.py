N = int(input())
S = list(input())
pre_word = str()
ans = 0

for i in range(N):
	if pre_word == S[i]:
		continue
	else:
		ans += 1
		pre_word = S[i]

print(ans)
