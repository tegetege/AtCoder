import sys

N = list(map(int, input()))
N_sur = list()
for i in N:
    N_sur.append(i % 3) # 余剰のリスト

if sum(N) % 3 == 0:
    print(0)
    sys.exit()

elif sum(N) % 3 == 1:
    if len(N) > 1 and 1 in N_sur:
        print(1)
        sys.exit()
    elif len(N) > 2 and N_sur.count(2) >= 2:
        print(2)
        sys.exit()
    else:
        print(-1)
        sys.exit()

elif sum(N) % 3 == 2:
    if len(N) > 1 and 2 in N_sur:
        print(1)
        sys.exit()
    elif len(N) > 2 and N_sur.count(1) >= 2:
        print(2)
        sys.exit()
    else:
        print(-1)
        sys.exit()
