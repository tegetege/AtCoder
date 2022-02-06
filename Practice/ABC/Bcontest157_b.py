import sys

A = list()
for i in range(3):
    a = list(map(int,input().split()))
    A.append(a)
N = int(input())
for i in range(N):
    target = int(input())
    for a in range(len(A)):
        for k in range(len(A[a])):
            if target == A[a][k]:
                A[a][k] = 0

# 縦のビンゴを調べる
for i in range(3):
    if A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
        print('Yes')
        sys.exit()
# 横のビンゴを調べる
for i in range(3):
    if A[i][0] == 0 and A[i][1] == 0 and A[i][2] == 0:
        print('Yes')
        sys.exit()
# ナナメのビンゴを調べる
if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
    print('Yes')
    sys.exit()
if A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
        print('Yes')
        sys.exit()

print('No')
