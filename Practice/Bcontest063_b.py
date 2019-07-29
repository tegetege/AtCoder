S = list(input())
list_len = len(S)
if list_len == len(set(S)):
	print('yes')
else:
	print('no')