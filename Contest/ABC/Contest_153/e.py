# コスパの良い魔法で攻撃しつつける
# 最後だけ、最小の攻撃力で倒せる攻撃にする

max_cospa = 0
max_a = 0
max_b = 0
H,N = map(int,input().split())
magic_dict = dict()
# コスパの良い魔法を計算する
for i in range(N):
	A,B = map(int,input().split())
	if A not in magic_dict:
		magic_dict[A] = [B]
	else:
		dict_key = magic_dict[A]
		dict_key.append(int(B))
		dict_key.sort() # 昇順にソート
		magic_dict[A] = dict_key
	cospa = A/B
	if cospa >= max_cospa :
		max_cospa = cospa
		max_a = A
		max_b = B
# print(max_a,max_b)
amari_hp = H%max_a
# print('amari:',amari_hp)
# keyでソートする
magic_list = sorted(magic_dict.items(),key=lambda x:x[0])
# print(magic_list)
for i in range(len(magic_list)):
	if magic_list[i][0] > amari_hp:
		last_attack = magic_list[i][1][0]
		break

print(int(H/max_a)*max_b) if H%max_a == 0 else print((int(H/max_a)*max_b)+last_attack)
