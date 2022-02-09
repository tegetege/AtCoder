n = int(input())
many = 10**9 + 1
for i in range(n):
    a, p, x = map(int, input().split())
    a += 0.5
    # print(a, x)
    if a <= x:
        many = min(many, p)
print(-1) if many == 10**9 + 1 else print(many)