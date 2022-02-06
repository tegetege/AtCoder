number = list(map(int,input().split()))
count = 0
while True:
	if len(set(number)) == 1:
		break
	number.sort()
	if number[0] == number[1]:
		number[0] += 1
		number[1] += 1
		count+=1
	else:
		number[0] += 2
		count+=1

print(count)
