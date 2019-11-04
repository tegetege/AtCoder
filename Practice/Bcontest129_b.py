N = int(input())
W = list(map(int,input().split()))
abs_list = list()
for i in range(len(W)):
	abs_list.append(abs(sum(W[:i+1])-sum(W[i+1:])))
print(min(abs_list))