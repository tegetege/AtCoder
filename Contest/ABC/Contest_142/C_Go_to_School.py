N = int(input())
A = input()
for i in range(1,N+1):
	#任意の要素のindexを標準出力
	print(int(A.index(str(i))/2)+1, end=' ')