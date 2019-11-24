N,T = map(int,input().split())
t   = list(map(int,input().split()))


time = 0 # お湯が出てる累計時間、一回目
for i in range(N-1):
	# print('ボタンを押す時間:',t[i])
	if abs(t[i+1]-t[i]) > T:
		time += T
	else:
		time += abs(t[i+1]-t[i])
	# print('累計:',time)

print(time+T)


















'''
t_  = list()
time = 0
ans_time = 0

for i in range(len(t)):
	if time + T > t[i]:
		t_.append(t[i])
		continue
	elif time + T == t[i]:
		time = t[i]
		t_.append(t[i])
		continue
	else:
		time = t[i]
		t_.append(-1)
		t_.append(t[i])
		continue
t_.append(-1)

target = list()
for i in range(len(t_)):
	if t_[i] != -1:
		target.append(t_[i])
	else:
		ans_time += abs(target[-1]-target[0])+T
		target = list()

print(ans_time)
'''