n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = ''
for i in range(n):
    if a[i] != x:
        ans += str(a[i]) + ' '
print(ans)