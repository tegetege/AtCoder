'''
期待値
E[X] = sum(1:N)/N
'''

N,K = map(int,input().split())
p = list(map(int,input().split()))

# 期待値のリスト生成
ex_list = list()
for i in range(len(p)):
	ex_list.append(sum(range(1,p[i]+1))/p[i])

ans = 0
for i in range(N-K+1):
	ex = sum(ex_list[i:i+K])
	if ans < ex:
		ans = ex

print(ans)