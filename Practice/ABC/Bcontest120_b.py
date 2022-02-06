A,B,K = map(int,input().split())
ans_list = list()
for i in range(1,min(A,B)+1):
	if A%(i) == 0 and B%(i) == 0:
		ans_list.append(i)
print(ans_list[-1*K])