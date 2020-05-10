import sys
S = list(input())
T = list(input())

for i in range(len(S)):
    if S[i] != T[i]:
        print('No')
        sys.exit()

print('Yes')
