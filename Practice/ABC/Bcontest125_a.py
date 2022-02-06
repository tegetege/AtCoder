A,B,T = map(int,input().split())
time = A
count = 0
while time <= T+0.5 :
	time += A
	count += 1

print(B*count)