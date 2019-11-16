N = int(input())
s = list()
for i in range(N):
	s.append(list(input()))
s_90 = list()

# # 90度時計回りに回転した時の配列を求める
# for i in range(len(s[0])):
# 	row = list()
# 	for j in range(N-1,-1,-1):
# 		row.append(s[j][i])
# 	s_90.append(row)

import numpy as np 
s_90 = np.rot90(s,k=-1)


for i in range(len(s_90)):
	print(''.join(s_90[i]))


