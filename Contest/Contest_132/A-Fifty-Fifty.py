'''
インプットSをLIST→SETに変換して、
その長さが2の時、YES.
それ以外はNo.
'''

Inp = list(input())
Inp.sort()

if len(set(Inp)) == 2: print('Yes')
else: print('No')




'''
これでWAとなるのは、後々検証
if Inp[0] == Inp[1] and Inp[2] == Inp[3]:
	print('Yes')

else:
	print('No')
'''