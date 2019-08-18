import sys
N = int(input())
v = list(map(int,input().split()))
max_num = max(v)
v.remove(max(v))

if N >2:
	x = min(v)
	v.remove(min(v))
	y = min(v)
	v.remove(min(v))
	value = (x+y)/2
	# print(x,':',y,'→',value)
	while len(v) != 0:
		target = value
		value = (value+min(v))/2
		# print(target,':',min(v),'→',value)
		v.remove(min(v))

	print((value+max_num)/2)
	sys.exit()

else:
	print((max_num+v[0])/2)
	sys.exit()
