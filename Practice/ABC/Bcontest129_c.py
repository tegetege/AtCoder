'''
参照：./img/Bcontest129_c.png
'''

N,M = map(int,input().split())
step_list = list(range(N+1))
denger_list = list()
for i in range(M):
	#連続数値の場合、答えは0と表示するとTLEを
	#回避できるかもしれない
	denger_list.append(int(input()))


ppre_step = None
pre_step  = None
now_step  = 0

for i in range(N+1):
	if i == 0:
		continue
	if i == 1:
		if i not in denger_list:
			ppre_step,pre_step,now_step = pre_step,0,1

		if i in denger_list:
			ppre_step,pre_step,now_step = pre_step ,0,0

	if i == 2:
		if i not in denger_list:
			if 1 in denger_list:
				ppre_step,pre_step,now_step = pre_step,now_step,1	
			else:
				ppre_step,pre_step,now_step = pre_step,now_step,2
		if i in denger_list:
			ppre_step,pre_step,now_step = pre_step ,now_step,0

	else:
		#そのステップが危険でない場合、そこのステップ
		#への移動は、2つ前までの移動方法数の和となる
		if i not in denger_list:
			ppre_step = pre_step
			pre_step  = now_step
			now_step  = ppre_step + pre_step
		#そのステップが危険な場合、そこの値は
		#移動不可能なので0通りとなる
		elif i in denger_list:
			ppre_step = pre_step
			pre_step  = now_step
			now_step  = 0 
	# print('========')
	# print('i:',i)
	# print('ppre_step:',ppre_step)
	# print('pre_step:',pre_step)
	# print('now_step:',now_step)



print(now_step%1000000007)