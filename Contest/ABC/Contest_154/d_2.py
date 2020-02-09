'''
期待値
E[X] = sum(1:N)/N
'''

N,K = map(int,input().split())
p = list(map(int,input().split()))

ans = 0
ans_list = list()
for i in range(N-K+1):
	ex = sum(p[i:i+K])
	if ans < ex:	
		ans = ex
		ans_list = p[i:i+K]

ans_ex = 0
for i in range(K):
	ans_ex += sum(range(1,ans_list[i]+1))/ans_list[i]
print(ans_ex)
