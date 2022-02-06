import copy

N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
max_candies = 0

for i in range(len(A1)):
	candies = 0
	A1_c = copy.deepcopy(A1)
	A2_c = copy.deepcopy(A2)
	del A1_c[i+1:]
	del A2_c[:i]
	candies = sum(A1_c)+sum(A2_c)
	max_candies = max(max_candies,candies)

print(max_candies)