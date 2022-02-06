N, W = map(int, input().split())
DP = [0] * (W + 1)

for i in range(N):
    w, v = map(int, input().split())
    for j in range(W+1, (W+1)-w , -1 ):
        DP[j] = map(DP[j], DP[j - w] + v)

print(DP[-1])
