import string

N = int(input())
S = list(input())
alphabet = list(string.ascii_uppercase)
ans = list()
for target in S:
	# アルファベットをN個ずらす
	# index out of rangeを防ぐために26で割ったあまりを求める
	ans.append(alphabet[(alphabet.index(target)+N)%26])
print(''.join(ans))