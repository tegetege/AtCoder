A,B,K = map(int,input().split())
ans =list()

for i in range(A,A+K):
	if i <= B:
		ans.append(i)

for i in range(B-K+1,B+1):
	if A <= i:
		ans.append(i)
#リストをset化して、重複を取り除く
ans=list(set(ans))
ans.sort()	#昇順にソート

for i in ans:
	print(i)