A,B,C = map(int,input().split())
remnant = C - (A-B)
if remnant >= 0:
	print(remnant)
else:
	print(0)