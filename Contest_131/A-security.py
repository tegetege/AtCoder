from sys import stdin

def judge(S):
	S_list  = list(str(S))  #list化
	
	i_pure = None
	for i in S_list:
		if i == i_pure:
			return 'Bad'
		i_pure = i

	return 'Good'


# S = ['3776','8080','1333','0024']

S = stdin.readline()
# for s in S:
# 	print(judge(s))

print(judge(S))