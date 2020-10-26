# https://atcoder.jp/contests/dp/submissions/17657169

N = int(input())
info = list()
for i in range(N):
    row = list(map(int, input().split()))
    info.append(row)
dp = [[0] * 3 for i in range(N + 1)]
dp[0] = [0, 0, 0]
for i in range(1, N + 1):
    dp[i][0] = max(info[i - 1][0] + dp[i - 1][1], info[i - 1][0] + dp[i - 1][2])
    dp[i][1] = max(info[i - 1][1] + dp[i - 1][0], info[i - 1][1] + dp[i - 1][2])
    dp[i][2] = max(info[i - 1][2] + dp[i - 1][0], info[i - 1][2] + dp[i - 1][1])
print(max(dp[N]))
