N = int(input())

ans = 1
for i in range(1,N+1):
	if i*i <= N:
		continue
	else:
		ans = (i-1)**2
		break
print(ans)