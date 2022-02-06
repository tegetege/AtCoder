N = int(input())
S = list(map(str,input()))
target = len(set(S))
count = list()
for i in range(1,N):
	X = set(S[:i])
	Y = set(S[i:])
	# 対称差集合
	symmetric_difference = X ^ Y
	count.append(target - len(symmetric_difference))
	# print('X:',X,'Y:',Y)
	# print(len(symmetric_difference))
print(max(count))