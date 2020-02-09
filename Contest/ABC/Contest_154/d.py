'''
- 累積和
期待値
E[X] = sum(1:N)/N
'''

N,K = map(int,input().split())
p = list(map(int,input().split()))

# 期待値の累積和リストを生成
ex_list = list() 
for i in range(len(p)):
	if i != 0:
		ex_list.append(((1+p[i])/2)+ex_list[-1])
	else:
		ex_list.append((1+p[i])/2)

ans = ex_list[K-1]
for i in range(N-K):
	# print(i,ex_list[i],ex_list[i+K])
	ex = abs(ex_list[i] - ex_list[i+K])
	if ans < ex:
		ans = ex
print(ans)