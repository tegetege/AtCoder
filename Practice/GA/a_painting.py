# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a

H = int(input())
W = int(input())
N = int(input())

if N // H > N // W:
	print((N // W) + 1 ) if N % W != 0 else print(N // W)
else:
	print((N // H) + 1 ) if N % H != 0 else print(N // H)

# cylikさんの回答 こっちの方が一行でかけてて勉強になる
# print((N // max(H, W)) if N % max(H, W) == 0 else (N // max(H, W) + 1))

