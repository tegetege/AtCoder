n, x = map(int, input().split())
s = 0

for i in range(n):
    v, p = map(int, input().split())
    s += v * p
    if s > x * 100:
        print(i + 1)
        exit()
print(-1)