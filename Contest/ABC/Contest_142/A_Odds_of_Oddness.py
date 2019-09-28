N = int(input())
if N % 2 != 0:
	print((int(N/2)+1)/N)
else:
	#偶数
	print(int(N/2)/N)
