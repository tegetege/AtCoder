import copy

def cul_money(a_list):
	amount = 0
	a_list.insert(0,0)
	a_list.insert(len(a_list),0)
	it = iter(a_list)
	for x in it:
		'''
		a_listから2個ずつ取り出して絶対値の計算
		をする
		'''
		# print(x,next(it))
		amount += abs(x-next(it))

	return amount

N = int(input())
A = list(map(int,input().split()))

for i in range(len(A)) :
	a_list = copy.deepcopy(A) #値渡し
	a_list.pop(i)
	print(cul_money(a_list))
	# print('a_list:',a_list)
	# print('A:',A)
