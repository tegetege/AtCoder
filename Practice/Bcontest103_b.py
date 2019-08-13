import sys
S = list(input())
T = str(input())

for i in range(len(S)):
	mojiretsu = ''.join(S)
	if T == mojiretsu :
		print('Yes')
		sys.exit()
	else:
		#リストの入れ替えを行う
		target = S[-1]
		S.pop(-1)
		S.insert(0,target)

print('No')
