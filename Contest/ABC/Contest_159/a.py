import math
N, M = map(int,input().split())
ans = 0
# 偶数、偶数
if N >= 2:
    ans = math.factorial(N)/(2*math.factorial(N-2))
    
    # N*(N-1)/N
# 奇数、奇数
if M >= 2:
    ans += math.factorial(M)/(2*math.factorial(M-2))
print(int(ans))
