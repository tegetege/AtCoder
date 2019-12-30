l = list(map(int,input().split()))
l_set = set(l)

side_sum = 0
for i in l_set:
	side_sum += i * 2
for i in range(len(l)):
	side_sum -= l[i]
print(abs(side_sum-0))