S = list(map(str,input()))

S_pre = S[:int(len(S)/2)]
if len(S) % 2  == 0 : # 偶数
	S_aft = S[int(len(S)/2):]
else: # 奇数
	S_aft = S[int(len(S)/2)+1:]
S_aft.reverse() # 逆順
count = 0
for i in range(len(S_pre)):
	if S_pre[i] != S_aft[i]:
		count += 1

print(count)