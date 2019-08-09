import sys

rule = list(map(int,input().split()))
S = str(input())
S_list = list(S.split('-'))

for i in range(len(S_list)):
	hoge_list = list(S_list[i])
	if len(hoge_list) != rule[i]:
		print('No')
		sys.exit()
print('Yes')
