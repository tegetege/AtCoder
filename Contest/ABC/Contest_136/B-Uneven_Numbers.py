N = int(input())
count = 0

for i in range(N+1):
	if 1<=i and i<=9:
		count += 1
	elif 100<=i and i<=999:
		count += 1
	elif 10000<=i and i<=99999:
		count += 1

print(count)