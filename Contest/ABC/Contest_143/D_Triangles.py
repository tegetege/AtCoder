import itertools

N = int(input())
L = list(map(int,input().split()))
L.sort(reverse=True)
count = 0
target = list(itertools.combinations(L,3))

for i in target:
	a = i[0]
	b = i[1]
	c = i[2]
	if a < b+c and b < c+a and c < a+b :
		count+=1
print(count)


# for i in range(len(L)-2):
# 	a = L[i]
# 	for j in range(i+1,len(L)-1):
# 		b = L[j]
# 		for k in range(j+1,len(L)):
# 			if a - b < L[k]:
# 				count += 1
# 			else:
# 				break

# print(count)


# for i in range(len(L)-2):
# 	for j in range(i+1,len(L)-1):
# 		for k in range(j+1,len(L)):
# 			a = L[i]
# 			b = L[j]
# 			c = L[k]
# 			if a < b+c and b < c+a and c < a+b :
# 				count += 1
