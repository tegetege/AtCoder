# https://atcoder.jp/contests/dp/tasks/dp_b
import numpy as np

N,K = map(int, input().split())
h = np.array(list(map(int, input().split())))
dp = np.full(N,10**10)
dp[0] = 0
for i in range(1,N):
    start = max(0,i-K)
    dp[i] = min(dp[start:i]+np.abs(h[i]-h[start:i]))
    # for j in range(max(0,i-K),i):
    #     # print(h[j],':',h[i])
    #     dp[i] = np.fmin(dp[i], dp[j]+ np.abs(h[j]-h[i]))
    # print(dp)
print(int(dp[-1]))
