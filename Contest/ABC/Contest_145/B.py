import sys
N = int(input())
S = list(input())

if N % 2 == 0:
	T = S[:int(len(S)/2)]
	T_end = S[int(len(S)/2):]

	for i in range(len(T)):
		if T[i] != T_end[i]:
			print('No')
			sys.exit()

	print('Yes')
	sys.exit()
else:
	print('No')
