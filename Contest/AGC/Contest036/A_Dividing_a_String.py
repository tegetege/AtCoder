S = list(input())

pre_list = []
tar_list = [S[0]]
count = 1
i = 1
try:
	while i < len(S):
		pre_list = tar_list #一つ前のリストを引き継ぐ
		tar_list = []
		tar_list.append(S[i])
		i += 1
		#一緒だったら続ける
		while tar_list == pre_list:
			tar_list.append(S[i])
			i += 1
		#異なった時に止めてカウントをアップ
		# print(pre_list,':',tar_list)
		count += 1

except IndexError:
	pass
print(count)