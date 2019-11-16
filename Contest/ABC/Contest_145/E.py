from operator import itemgetter

def cul(menu):
	good = 0 # 美味しさ
	time = 0 # 時間
	for i in range(len(menu)):
		if time >= T-0.5:
			break
		else:
			good += menu[i][1]
			time += menu[i][0]
	return good


N,T = map(int,input().split())
menu = list()
for i in range(N):
	menu.append(list(map(int,input().split())))
# 時間が少ない順に計算
menu.sort() # 時間が少ない順にソート
good_1 = cul(menu)

# 満足度が多い順に計算
menu.sort(key=itemgetter(1),reverse=True)
good_2 = cul(menu)
print(max(good_1,good_2))

# 満足度と時間を考えてソート

# menu_1 = dict()
# for i in range(len(menu)):
# 	if abs(menu[i][1]-menu[i][0]) not in menu_1:
# 		menu_1[abs(menu[i][1]-menu[i][0])] = menu[i]
# print(menu_1)