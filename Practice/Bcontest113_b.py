N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
abs_dict = dict()
abs_list = list()

for i in range(N):
	temp_abs = abs(A-(T-H[i]*0.006)) 
	abs_dict[temp_abs] = i
	abs_list.append(temp_abs)
print(abs_dict[min(abs_list)]+1)