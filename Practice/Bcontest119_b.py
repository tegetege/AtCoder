N = int(input())
count = 0
for i in range(N):
	x = input().split()
	if x[1] == 'JPY':
		count += int(x[0])
	else:
		count += float(x[0])*380000.0
print(count)