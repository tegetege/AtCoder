'''
入力されたl_iをソートして、大きい順に
K個の和を求める
'''

N,K =map(int,input().split())
Int = list(map(int,input().split()))
Int.sort(reverse=True)
print(Int)
length = 0

for i in range(int(K)):
	length += int(Int[i])
print(length)