m, n = map(int,input().split())

if n == 0:
    print(1)

K = 1
while n > 1:
    if n % 2 != 0:
        K *= m
        m = m ** 2
        n = (n-1) // 2
    else:
        m = m ** 2
        n = n // 2

print(K * m)
