a,b,x = map(int,input().split())
#高さ
high = x / (a*a)
low = 2*x/b
volume = a*a*b

if high * 2 <= b:
	# 半分より少ない、三角形になる
	pass
else:
	# 半分より多く、台形になる
	pass