N,X = map(int,input().split())
target = list()
ans = 0
for i in range(N):
	target.append(int(input()))
X -= sum(target)
ans = len(target)
ans += int(X / min(target))
print(ans)