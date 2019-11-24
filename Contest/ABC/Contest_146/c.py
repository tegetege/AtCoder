A,B,X = map(int,input().split())
# d_Nの最大値を求める
d_N_max = X/B - (A/B)*1
# Nの最大値を求める
N = X/A - (B/A) # ココの誤差が悪さしているっぽい　input: 10 7 1021
print('d_N_max:',int(d_N_max))
print('N:',N)
d_N = len(list(str(int(N)))) # 桁数を求める
# print('桁数:',d_N)
if d_N <= int(d_N_max):
	if int(N) >= 1000000000:
		print(1000000000)
	else: 
		N_cost = A*int(N)+(B*d_N)
		print('N_cost:',A*int(N)+(B*d_N))
		if N_cost > X: # Nの価格がXを超える場合の補正
			N -= int((N_cost - X)/A)+1
		# print('N_cost:',A*int(N)+(B*d_N))
		print(int(N))

else:
	print('0')
