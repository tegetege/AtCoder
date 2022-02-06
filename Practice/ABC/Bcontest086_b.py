import sys

num = input().replace(' ','')
#最大100100の数にも対応できる様にfor文を回す必要がある
for i in range(1,340):
	if int(num) == i*i:
		print('Yes')
		sys.exit()
print('No')