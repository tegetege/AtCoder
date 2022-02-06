K,X = map(int,input().split())

K -= 1 
if  -1000000 <= X-K:
	start = X-K 
else:
	start = -1000000

if X+K <= 1000000:
	goal = X+K
else:
	goal = 1000000


ans = list(range(start,goal+1,1))
print(' '.join(map(str,ans))) 
