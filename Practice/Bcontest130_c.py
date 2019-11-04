W,H,x,y = map(int,input().split())

core = [W/2,H/2]
if x == core[0] and y == core[1]:
	print(round((W*H)/2,3),' 1')
else:
	print(str("{:.7f}".format((W*H)/2)),' 0')