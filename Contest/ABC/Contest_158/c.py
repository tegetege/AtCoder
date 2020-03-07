import sys
import math

A,B = map(int,input().split())
# 四捨五入
if A * (100/8) - int(A * (100/8)) >=0.5:
    target_8  = math.floor(A * (100/8)) + 1
else:
    target_8  = math.floor(A * (100/8))

# 四捨五入
if A * (100/10) - int(A * (100/10)) >=0.5:
    target_10 = math.floor(B * (100/10)) + 1
else:
    target_10 = math.floor(B * (100/10))

if math.floor(target_8*0.1) == B :
    print(target_8)
    sys.exit()
elif math.floor(target_10*0.08) == A :
    print(target_10)
    sys.exit()
else:
    print('-1')
    sys.exit()