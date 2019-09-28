import sys

N,K,Q = map(int,input().split())
A_list = [int(sys.stdin.readline()) for i in range(Q)]

if K - Q > 0 :
	for i in range(N):
		print('Yes')
	sys.exit()

else:
	for i in range(N):
		if K - (Q-A_list.count(i+1)) > 0:
			print('Yes')
		else:
			print('No')