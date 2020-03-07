S = str(input())
Q = int(input())
count = 0
for i in range(Q):
    Query = list(input().split())
    if Query[0] == '1':
        count += 1 #countが偶数:正 奇数:逆
    else: # T = '2'
        if Query[1] == '1':
            if count % 2 == 0:
                S = Query[2] + S
            else:
                target = Query[2][::-1]
                S = S + target
        else: # F = '2'
            if count % 2 == 0:
                S += Query[2]
            else:
                target = Query[2][::-1]
                S = target + S
if count % 2 == 0:
    print(S)
else:
    print(S[::-1])