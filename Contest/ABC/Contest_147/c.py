import sys

# 入力
N = int(input())
x_all = dict()
for i in range(N):
	A = int(input())
	for j in range(A):
		x,y = map(int,input().split())
		if x in x_all:
			x_all[x].append(y)
		else:
			x_all[x] = [y]

# 全部が1の場合
roop = 0
for k,v in x_all.items():
	v_set = set(v)
	v_list = list(v_set)
	if len(v_set) == 1 and v_list[0] == 1 :
		roop += 1
if roop == N :
	print(roop)
	sys.exit()

# 全部が0の場合
roop = 0
for k,v in x_all.items():
	v_set = set(v)
	v_list = list(v_set)
	if len(v_set) == 1 and v_list[0] == 0:
		roop += 1
if roop == N:
	print(roop-1)
	sys.exit()

# 全部が[0,1]入っている場合
for k,v in x_all.items():
	v_set = set(v)
	if len(v_set) == 2:
		roop += 1
if roop == N:
	print(0)
	sys.exit()

# とりあえず1しかない人をカウント
count = 0
for k,v in x_all.items():
	v_set = set(v)
	v_list = list(v_set)
	if len(v_set) == 1 and v_list[0] == 1 :
		count += 1
if count != 0:
	print(count)
	sys.exit()
print(x_all)
print(count)