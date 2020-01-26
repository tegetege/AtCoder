N = int(input())
restaurants = dict()
ans = list()
target = list()
for i in range(N):
	S = list(map(str,input().split()))
	if S[0] not in restaurants :
		restaurants[S[0]] = [int(S[1])]
	else:
		dict_key = restaurants[S[0]]
		dict_key.append(int(S[1]))
		dict_key.sort(reverse=True)
		restaurants[S[0]] = dict_key
	target.append(S[0]+' '+S[1])


restaurants_sorted = sorted(restaurants.items(), key=lambda x:x[0])
for idx in range(len(restaurants_sorted)):
	for i in range(len(restaurants_sorted[idx][1])):
		print(target.index(restaurants_sorted[idx][0]+' '+str(restaurants_sorted[idx][1][i]))+1)