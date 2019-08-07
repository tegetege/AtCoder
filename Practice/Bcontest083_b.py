N,A,B = map(int,input().split())
N_list = list()

for i in range(N+1):
	# 各桁をmap関数でリスト化する
	array = list(map(int,str(i)))
	if sum(array) >= A and sum(array) <= B:
		N_list.append(i)

print(sum(N_list))
