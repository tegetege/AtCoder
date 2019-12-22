N = int(input())
S,T = map(list,input().split())
ans = list()
for i in range(N):
	ans.append(S[i])
	ans.append(T[i])

print(''.join(ans))
