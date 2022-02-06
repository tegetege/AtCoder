# https://qiita.com/wasshoy/items/b47da0eb043a6c173c97#c

import sys
n, m = map(int, input().split())
sc = list()
for i in range(m):
    sc.append(list(map(int, input().split())))

ans = float('inf')
k = 0
if n == 2: k = 10
elif n == 3: k = 100
for i in range(k, 1000):
    flg = True
    for s, c in sc:
        if list(str(i))[s - 1] == str(c): 
            continue
        else:
            flg = False
    if flg:
        print(i)
        sys.exit()
print(-1)
