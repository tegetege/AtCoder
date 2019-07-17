'''
(1)入力されたリストを半分にする
(2)後半のリストを反転して、前半リストとの一致を判定する

'''

def judge(num):
	num_list_pre =list()
	num_list_late =list()
	num_list = list(str(num))
				 
	num_list_pre.extend(num_list[:int(len(num_list)/2):])
	num_list_late.extend(num_list[int(len(num_list)/2)+1:])
	# print('reverse:',list(reversed(num_list_late)))
	if num_list_pre == list(reversed(num_list_late)):
		return True
	else:
		return  False



A,B = map(int,input().split())
count =0

for i in range(A,B+1):
		if judge(i):
			 count +=1


print(count)