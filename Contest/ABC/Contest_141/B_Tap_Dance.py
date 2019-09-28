import sys
S = list(input())

#奇数
odd_list = ['R','U','D']
#偶数
even_list = ['L','U','D']

for i in range(len(S)):
	#偶数
	if (i+1) % 2 == 0:
		if S[i] not in even_list:
			print('No') 
			sys.exit()
	#奇数
	else:
		if S[i]  not in odd_list:
			print('No')
			sys.exit()

print('Yes')