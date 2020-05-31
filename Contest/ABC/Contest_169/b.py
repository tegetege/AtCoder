import sys
N = int(input())
A = list(map(str,input().split()))
for i in range(N):
    if A[i] == '0':
        print('0')
        sys.exit()

ans = 1
for i in range(N):
    ans *= int(A[i])
    if ans > 1000000000000000000:
        print(-1)
        sys.exit()

print(ans)
