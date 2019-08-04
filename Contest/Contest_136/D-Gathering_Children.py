def cul(target,status):
	print(target)
	ans_list = list()
	max_num = max(target.count('R'),target.count('L'))
	need_count = max_num-1 #全てがRLの真ん中に集まるのに必要な回数
	#need_countが奇数の場合、最後は反転する
	print(target.count('R'))
	print(target.count('L'))
	print(target)
	'''
	最後に答えとして出力するリストを作成する必要がある
	target.count('RとL')と0を使ったリスト形成
	'''

	return ans_list


S = list(input())
target = list()
ans = list()
status =0
key = S[0]
for i in S:
	if status == 0:
		if key == i:
			target.append(i)
		else:
			status = 1
			key = i
			target.append(i)
	elif status == 1:
		if key == i:
			target.append(i)
		else:
			#targetを計算する関数にぶん投げる
			cul(target,status)
			status = 0
			key = i
			target = list()
			target.append(i)