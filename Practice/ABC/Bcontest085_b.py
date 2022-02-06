N= int(input())
d = list()
for i in range(N):
	d.append(int(input()))

d_set = set(d)
d_list = list(d_set)
d_list.sort()

print(len(d_list))
