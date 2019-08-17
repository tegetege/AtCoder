import itertools
import sys

N = int(input())
A_list = list(map(int,input().split()))
B_list = list()
for i in A_list:
	B_list.append(bin(i))

bin_0 = bin(A_list[0])
bin_2 = bin(A_list[2])

ans = bin(A_list[0]^A_list[2])
if ans in B_list:
	print('Yes')
	sys.exit()
else:
	count = 0 
	for i in itertools.combinations(A_list,2):
		count += 1
		if count <= 30:
			ans = bin(i[0]^i[1])
			if ans in B_list:
				print('Yes')
				sys.exit()
			else:
				continue
		else:
			break
print('No')
