import math
import itertools

N , D  = map(int,input().split())
X_list = list() 
count = 0

for i in range(N):
	Inp = list(map(int,input().split()))
	X_list.append(Inp)

for i in itertools.combinations(X_list,2):
	distance = 0
	for j in range(len(i[0])):
		distance += abs(i[0][j]-i[1][j])**2
	if math.sqrt(distance) % 1 == 0:
		count += 1 
print(count)


# try:
# 	for i in range(0,N):
# 		distance = 0 
# 		for j in range(len(X_list[i])):
# 			distance += abs(X_list[i][j]-X_list[i+1][j])**2
# 		if math.sqrt(distance) % 1 == 0:
# 			print('X:',X_list[i][j],X_list[i+1][j])
# 			count += 1 



# except IndexError:
# 	distance = 0 
# 	for j in range(len(X_list[i])):
# 		print('X:',X_list[i][j],X_list[0][j])
# 		distance += abs(X_list[i][j]-X_list[0][j])**2
# 	if math.sqrt(distance) % 1 == 0:
# 		print('X:',X_list[i][j],X_list[0][j])
# 		count += 1 
