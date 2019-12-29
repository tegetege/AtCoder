N, K = map(int,input().split())
R, S, P = map(int,input().split())
T = list(input())

ans = list()
score = 0
for i in range(N):
	if K == 1:
		K = 2
	if i < K-1:
		# K回までは全部勝つ手を出すことができる
		if T[i] == 'r':
			score += P
			ans.append('p')
		elif T[i] == 's':
			score += R
			ans.append('r')
		else:
			score += S
			ans.append('s')
	else:
		# K回前の手を見る必要がある
		if T[i] == 'r' and ans[i-K] != 'p':
			score += P
			ans.append('p')
		elif T[i] == 's' and ans[i-K] != 'r':
			score += R
			ans.append('r')

		elif T[i] == 'p' and ans[i-K] != 's':
			score += S
			ans.append('s')
		else:
			if T[i] == 'r':
				ans.append('r')
			elif T[i] == 's':
				ans.append('s')
			else:
				ans.append('p')
	print(T[i],':',score)
	print(ans)
print(score)