N = int(input())
N_list = list(str(N))
S_n = 0
for i in range(len(N_list)):
	S_n += int(N_list[i])
if N % S_n == 0:
	print('Yes')
else:
	print('No')