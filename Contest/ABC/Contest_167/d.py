from collections import deque
import sys

N,K = map(int,input().split())
A = list(map(int,input().split()))

# ループを見るける
target = deque()
target_s = set()
target.append(1)
target_n = A[0]
for i in range(K):
    before = len(target_s)
    target_s.add(target_n)
    if len(target_s) != before:
        target.append(target_n)
        # target_s.add(target_n)
        target_n = A[target_n-1]
    else:
        if target[-1] != 1:
            target.append(target_n)
        t = target.pop()
        t = target.index(t)
        if t != 0:
            K -= len(target)
        K = K%(len(target) - t)
        print(target[K+t])
        sys.exit()

print(target[-1])

