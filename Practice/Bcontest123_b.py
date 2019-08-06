
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

target = [A,B,C,D,E]
num_list = [1,2,3,4,5,6,7,8,9,0]

ans_sur  = num_list.index(0)
ans = int()

#num_listのindexが最小の値をリストの最後に
#したいのでその判定
for i in target:
	number = num_list.index(i%10)
	if ans_sur >= number:
		ans_sur = number
		ans = i

target.pop(target.index(ans))
target00 = list()
#上のfor文でlistからpopされなかった要素について
#1の位を00秒に合わせる
for i in target:
	if i % 10 != 0:
		#00秒に合わせる
		target00.append(i+(10-i%10))
	else:
		#1桁台が0の時は何もせずにappend
		target00.append(i)

target00.append(ans)
print(sum(target00))