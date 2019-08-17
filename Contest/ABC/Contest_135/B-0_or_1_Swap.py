N = int(input())
P = list(map(int,input().split()))
ANS = list(range(1,N+1))
count = 0 
dif = list()

for i in range(N):
	if ANS[i] != P[i]:
		count += 1 
		dif.append(P[i])

if count == 0 :
	print('YES')
elif count == 2 :
	print('YES')
else:
	print('NO')