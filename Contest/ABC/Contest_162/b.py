
N = int(input())
ans = 0
for i in range(1,N+1):
    # if (i % 3 is 0) or  (i % 5 is 0): なぜこれがダメ？
    if i % 3 != 0 and i % 5 != 0:
        ans += i
print(ans)
