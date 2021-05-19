s = str(input())
t = str(input())
DP = list()
for i in range(len(s) + 1):
    horizon = list()
    for j in range(len(t) + 1):
        horizon.append("")
    DP.append(horizon)


for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i - 1] == t[j - 1]:
            DP[i][j] = max(DP[i][j], DP[i - 1][j] + s[i - 1])
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
print(DP[len(s)][len(t)])
