N = int(input())
act = list()
#rangeを利用するため、数合わせで-1をつける
if N%2 ==0:
	line = int(N/2)-1
else:
	line = int(N/2)

for i in range(N,line,-1):
	if N % i == 0:
		j = int(N/i)
		print(i,':',j)
		act.append(abs(j-1)+abs(i-1))
print(min(act))