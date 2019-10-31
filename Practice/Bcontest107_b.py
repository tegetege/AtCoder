H,W = map(int,input().split())
a = list()
#入力
for i in range(H):
	a_line = list(input())
	a.append(a_line)

ans = list()
#全部白の行を削除
for line in a:
	if {'#'} <= set(line):
		ans.append(line)

column_list = list()
# 列
for column in range(len(ans[0])):
	count = 0
	# 行
	for line in ans:
		if line[column] == '.':
			count += 1
		else:
			count = 0
			break
	if count == len(ans):
		column_list.append(column)

column_list.sort(reverse=True)

for line_num in range(len(ans)):
	for pop_column in column_list:
		ans[line_num].pop(pop_column)

for line in ans:
	print(''.join(line))
'''
# 全て白の列を求める
column_list = list()
# 列
for column in range(len(a[0])):
	count = 0
	# 行
	for line in a:
		if line[column] == '.':
			count += 1
		else:
			count = 0
			break
	if count == len(a):
		column_list.append(column)
ans = list()
# 全て白の行を削除
for pop_column in column_list:
	for line_num in range(len(a)):
		a[line_num].pop(pop_column)
		if '#' in set(a[line_num]):
			ans.append(a[line_num])

	
for line in ans:
	print(''.join(line))

'''
