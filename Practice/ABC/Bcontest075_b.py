H,W = map(int,input().split())
S = list()
for i in range(H):
	S.append(list(input()))
ans = list()

for i in range(len(S)):
	row = list()
	for j in range(len(S[i])):
		if S[i][j] == '#': # 爆弾だったら#を出力
			row.append('#')
			continue # この後のfor文内の処理をスキップ
		count = 0
		check_list =[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
		for c in range(len(check_list)):
			if check_list[c][0] >= 0 and check_list[c][0] < len(S) and check_list[c][1] >= 0 and check_list[c][1] < len(S[i]):
				if S[check_list[c][0]][check_list[c][1]] == '#':
					count += 1
		row.append(str(count))
	print(''.join(row))