target = list(map(int,input().split()))
target.sort(reverse=True)
print((target[0]*10+target[1])+target[2])