'''
リストを逆順に見ていく
gap = H[i-1] - H[i]
gapが2以上の場合は'No'
gapが1以上の場合はH[i-1]を-1して元の位置に
入力する
'''

import sys


N = int(input())
H = list(map(int,input().split()))
for i in reversed(range(N)):
	if i != 0:
		gap = H[i-1] - H[i]
		if gap <= 0:
			continue
		elif gap == 1:
			H[i-1] -= 1
		else:
			print('No')
			sys.exit()
	else:
		pass
print('Yes')