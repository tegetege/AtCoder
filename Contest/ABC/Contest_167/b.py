import sys
A,B,C,K = map(int,input().split())
ans = 0

if K >= A:
    ans += A
else:
    ans += K
K -= A
if  K <= 0:
    print(ans)
    sys.exit()
K -= B
if K > 0:
    if K >= C:
        ans += (-1*C)
    else:
        ans += (-1*K)
print(ans)
