# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp

N, W = map(int, input().split())
items = list()
for i in range(N):
    item = list(map(int, input().split()))
    items.append(item)

DP = [[0 for j in range(W + 1)] for i in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j < items[i][1]:
            DP[i + 1][j] = DP[i][j]
        else:
            DP[i + 1][j] = max(DP[i][j], DP[i][j - items[i][1]] + items[i][0])

print(DP[N][W])
