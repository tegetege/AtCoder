#問題の通りにアルゴリズムを組めば解ける
#ループが偶数回の時にAを計算して、奇数回の時にBを計算する
A, B, K= map(int, input().split())

for i in range(int(K)):
	if i % 2 == 0:
		if A % 2 != 0 :	A += -1
		B += A/2
		A -= A/2
	else:
		if B % 2 != 0 :	B+= -1
		A += B/2
		B -= B/2
print(int(A) , int(B))