import sys
A , B = map(int,input().split())

socket = 0
count  = 0
#最初についている1口で足りるとき
if B == 1:
	print(0)
	sys.exit()

#電源タップを追加する時
while True:
	count  += 1
	socket += A-1
	if B - socket <= 1:
		print(count)
		sys.exit()

# if B == 1:
# 	print(0)
# 	sys.exit()

# elif B - int(B/(A-1))*(A-1) > 1:
# 	ans = int(B/(A-1))+1
# 	print(ans)
# 	sys.exit()
# else:
# 	print(int(B/(A-1)))