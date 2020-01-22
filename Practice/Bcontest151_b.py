N,K,M = map(int,input().split())
A = list(map(int,input().split()))
target = M*N  # 取得するべき点数
if sum(A)+K >= target:
	if sum(A) >= target:
		print(0)
	else:
		print(target-sum(A)) 
else:
	print(-1)