
able = list()
for i in range(103):
    able.insert(i, i-1)

X,N = map(int,input().split())
p = list(map(int,input().split()))
for i in range(len(p)):
    able.remove(p[i])

target = 1000
ans = 1000
for i in range(len(able)):
    
    if (target > abs(X - able[i])):
        # if (target == abs(X - able[i])): 
        #     ans = min(target, able[i])
        # else:
        target = abs(X - able[i])
        ans = able[i]
    
    # print(able[i], abs(X - able[i]), ans)

print(ans)
