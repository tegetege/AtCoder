import sys
import copy

#任意の数の倍数リストを作成する
def make_multiple(N,target):
	multiple_list = list()
	for i in range(1,N+1): #この書き方って0も入るじゃない??
		if i % target == 0:
			multiple_list.append(i)
			break
	return multiple_list



N = int(input())
a = list(map(int,input().split()))

#全て0の時はそのまま0を表示して終了
a_c = copy.deepcopy(a)
a_s =set(a_c)
a_c = list(a_s)
if len(a_c) == 1 and a_c[0] == 0:
	print(0)
	sys.exit()

a.insert(0,0) #便宜上一番最初に0をinsert、最後にpopする

for i in range(len(a)):
	target_list = list()
	if a[i] != 0:
		# print('a[',i,']:',a[i])
		target_list =make_multiple(N,a[i])
		# if len(target_list) 
		# print(target_list,':',len(target_list))
		# print(len(target_list),'%',2,'=',len(target_list)%2)
		print(1)
		print(target_list[0])