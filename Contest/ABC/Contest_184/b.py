N, X = map(int, input().split())
S = list(input())

for i in range(len(S)):
    if S[i] == 'o':
        X += 1
    else:
        X = max(0, X - 1)

print(X)
