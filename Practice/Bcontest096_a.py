a,b = map(int,input().split())
if a <= b: # 月の数より、日にちの数の方が大きい場合
 	print(a)
else:
 	print(a-1)