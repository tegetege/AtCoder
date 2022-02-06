D,N = map(int,input().split())
# 100番目はすなわち、100で割り切れるので+1番目とする
if N == 100:
	N += 1
target = 100 ** D
print(N*target)