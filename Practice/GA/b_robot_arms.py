N = int(input())
Inp = list()
for i in range(N):
    x , l = list(map(int,input().split()))
    Inp.append([x-l,x+l])
# 右腕を基準にソートする
robots = sorted(Inp, key=lambda x: x[1])
# print(robots)

ans = 0
now = -float('inf')
for left,right in robots:
    if left >= now:
        ans += 1
        now = right

print(ans)
