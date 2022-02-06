n = list(input())
time = 100
ans = 0
for i in range(len(n)):
	if n[i] == '1':
		ans += 9 * time
	elif n[i] == '9':
		ans += 1 * time 
	else:
		ans += int(n[i])*time
	time /= 10

print(int(ans))