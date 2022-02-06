from datetime import datetime

target = datetime(2019,4,30)

S = str(input())
S_date = datetime.strptime(S,'%Y/%m/%d')

if S_date <= target:
	print('Heisei')
else:
	print('TBD')