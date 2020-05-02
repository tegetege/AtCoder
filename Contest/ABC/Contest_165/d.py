import math
A,B,N = map(int,input().split())
x = 0
# Bに対して一番余剰が大きくなる数字をとりたい
if B <= N:
    x = B-1
else:
    x = N
print(math.floor((A*x)/B)-A*math.floor(x/B))
