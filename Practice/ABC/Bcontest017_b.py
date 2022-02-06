import sys

# ch のジャッジをする関数
def judge_ch(X_1,X_2):
	if X_1 == 'c' and X_2 == 'h':
		return True
	else:
		return False


X = list(input())
if len(X) == 0:
	print('YES')  
	sys.exit()

for i in range(len(X)):
	if X[i] == 'o' or X[i] == 'k' or X[i] == 'u':
		True
	elif X[i] == 'c' and judge_ch(X[i],X[i+1]):
		True
	elif X[i] == 'h' and judge_ch(X[i-1],X[i]):
		True
	else:
		print('NO')
		sys.exit()
print('YES')
