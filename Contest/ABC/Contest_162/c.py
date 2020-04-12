from math import gcd
K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        ab = gcd(i,j)
        if ab == 0:
            continue
        for k in range(1,K+1):
            ans += gcd(ab,k)
print(ans)
