import sys
S = list(input())
S = [S[0]+S[1],S[2]+S[3]]
month = ['01','02','03','04','05','06','07','08','09','10','11','12']

# 月表示、年表示についてのステータス
# [前表示、後ろ表示]
mon = [0,0]
yer = [0,0]

if S[0] in month:
	mon[0] = 1
if S[1] in month:
	mon[1] = 1


if mon[0] == 1 and mon[1] == 1:
	print('AMBIGUOUS')
	sys.exit()
if mon[0] == 1:
	print('MMYY')
	sys.exit()
if mon[1] == 1:
	print('YYMM')
	sys.exit()
else:
	print('NA')
	sys.exit()
