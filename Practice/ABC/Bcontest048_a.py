target = list(map(str,input().split()))
ans = str()
for i in range(len(target)):
	ans += list(target[i])[0]
print(ans)