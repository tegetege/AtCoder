n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        ans += 1
        a[i] -= 1
    if a[i] % 3 == 2:
        ans += 2

print(ans)
