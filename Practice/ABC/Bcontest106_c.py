#このままだと桁計算が全然できていない
#5000兆回掛け算を行うと計算時間に収まらない

S = list(map(int,input()))
K = map(int,input())

S_cul = dict()
digit_list = list()
# day = 5000000000000000
day = 5000

for i in range(len(S)):
	for j in range(day):
		cul_digit = S[i]*S[i]
	cul_digit = cul_digit * 1000000000000
	print(S[i],':',cul_digit)


# for i in range(len(S)):
# 	cul_digit = S[i]*day
# 	if i-1 != -1:
# 		digit_list.append(cul_digit + digit_list[i-1])
# 	else:
# 		digit_list.append(cul_digit)

# print(digit_list) 