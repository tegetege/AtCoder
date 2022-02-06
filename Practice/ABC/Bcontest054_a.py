A,B = map(int,input().split())
card=[2,3,4,5,6,7,8,9,10,11,12,13,1]
if card.index(A) > card.index(B):
	print('Alice')
elif card.index(A) == card.index(B):
	print('Draw')
else:
	print('Bob')