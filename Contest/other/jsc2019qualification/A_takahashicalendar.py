M,D = map(int,input().split())

count = 0
for m in range(2,M+1):
	for d in range(22,D+1):
		d_list = list(str(d))
		if int(d_list[1])*int(d_list[0]) == int(m) and int(d_list[1])>=2 and int(d_list[0])>=2:
			count +=1

print(count)