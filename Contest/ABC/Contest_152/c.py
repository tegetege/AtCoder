N = int(input())
P = list(map(int,input().split()))

min_count = P[0]
ans_count = 0
for i in range(N):
	# 最小値を取得
	# 多分このmin()を使うとTLE
	# min_count = min(P[0:i+1])
	if P[i] <= min_count:
		min_count = P[i]
		ans_count += 1



print(ans_count)