s= list(map(str,input().split()))
ans = ''
# 一文字目をとってきて大文字にする
for i in range(len(s)):
	s_list = list(s[i])
	ans += s_list[0].upper()
print(ans)