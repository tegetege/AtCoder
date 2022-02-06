N,S,T = map(int,input().split())
W = int(input())
# 1日目の体重の判定
if S <= W and W <= T:
	count = 1 
else:
	count = 0
# 1日目以降の体重の判定
for i in range(N-1):
	gap = int(input())
	W += gap
	if S <= W and W <= T:
		count += 1
print(count) 