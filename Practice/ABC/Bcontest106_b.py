N= int(input())
ans = 0

#Ｎまでの範囲で奇数のみ回す
for i in range(1,N+1,2):
	# print(i)
	count=0	 
	#奇数のみを考えるので、1-200の間の奇数だけで考える
	for j in range(1,200,2):
		if j <= i and i % j ==0:
			# print('j:',j)
			count += 1
		else:
			continue
	if count == 8:
		ans += 1


print(ans)
