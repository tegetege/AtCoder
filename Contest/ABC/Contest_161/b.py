import numpy as np

N,M = map(int,input().split())
A = np.array(list(map(int,input().split())))

target = np.sum(A)
ans = 0
for i in range(N):
    if A[i] >= target/(4*M):
        ans += 1
print('Yes') if ans >= M else print('No')
