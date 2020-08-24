W = list(input())
target = ['a','i','u','e','o']
ans = str()
for i in range(len(W)):
    if W[i] not in target:
        ans += W[i]

print(ans)
