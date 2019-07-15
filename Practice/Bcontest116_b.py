def f(n):
	if n % 2 == 0:
		return int(n/2)
	else:
		return int(3*n+1)

a_list = [int(input())]

count = 0
while True:
	target = f(a_list[-1])
	if target in a_list:
		a_list.append(target)
		print(len(a_list))
		break
	else:
		a_list.append(target)