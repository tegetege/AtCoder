def counting(tar_word,tar_list):
	count = 0
	for i in range(len(tar_list)):
		if tar_word == tar_list[i]:
			count += 1
	return count

# 青いカード(1円加算)
N = int(input())
s = list()
for i in range(N):
	s.append(str(input()))
# 赤いカード(1円損失)
M = int(input())
t = list()
for i in range(M):
	t.append(str(input()))
target = s+t
target = set(target)
target = list(target)

ans = list()
for tar in target:
	count = 0
	count += counting(tar,s)
	count -= counting(tar,t)
	ans.append(count)

print(max(ans)) if max(ans) >= 0 else print(0)