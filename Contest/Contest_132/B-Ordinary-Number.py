'''
pを3つずつ取り出して、リストに入れた後、ソートする
あらかじめ取り出していたp_iの数を利用してif文条件で
判定する
'''

N = input()
P = list(input().split())
count = 0

for i in range(len(P)-2) :
	judge_list = list() 
	midle = int(P[i+1])
	judge_list.extend([int(P[i]),int(P[i+1]),int(P[i+2])])
	judge_list.sort()

	if midle == judge_list[1]:
		count+=1
print(count)