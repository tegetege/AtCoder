import itertools


def judge(judge_list):
	for i in range(len(judge_list)-1):
		if judge_list[i+1]-judge_list[i] >2:
			return False
	return True


N,M = map(int,input().split())
step_list = list(range(N+1))

for i in range(M):
	step_list.remove(int(input()))

count = 0
ans_list = list()
for i in range(N,int((N+1)/2),-1):
	for i in itertools.combinations(step_list,i):
		if judge(i):
			if N in i and 0 in i :
				ans_list.append(i)

print(len(ans_list)%1000000007)