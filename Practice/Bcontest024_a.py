A,B,C,K = map(int,input().split())
S,T = map(int,input().split())

if S+T >= K:
	# 団体料金設定
	A -= C
	B -= C
price = S*A + T*B

print(price)