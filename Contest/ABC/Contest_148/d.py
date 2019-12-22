N = int(input())
a = list(map(int,input().split()))
pre_len = len(a) # 最初の長さ
ans = list()

target = 1
for i in range(N):
	if a[i] == target:
		ans.append(i+1)
		target += 1


if len(ans) == 0:
	print(-1)
else:
	print(pre_len-len(ans))