N,M = map(int,input().split())
drink = dict()
# 価格をkey, 本数をlist形式でvalueで格納するdict()
for i in range(N):
	value,number = map(int,input().split())
	drink.setdefault(value,[]).append(number)

drink = sorted(drink.items()) # 価格(key)を昇順ソート
value = 0
for i in drink:
	# print('i:',i)
	if M <= i[1][0] : 
		print('value:',M*i[0])
		value += M*i[0]
		M -= M
	else:
		print('value:',i[0]*i[1][0])
		M -= i[1][0]
		value += i[0]*i[1][0]
	if M == 0:
		break
	print('残りM:',M)
	print('value_sum:',value)
print(value)	