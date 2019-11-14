X = int(input())
ans = set()
for i in range(1,int(X)):
	for j in range(2,11):
		if i**j <= X:
			ans.add(i**j)

ans_list = list(ans)
if len(ans_list)==0:
	print(1)
else:
	print(max(ans_list))