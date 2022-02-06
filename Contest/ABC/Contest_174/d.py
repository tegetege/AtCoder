import sys

def check(c):
    for j in range(len(c)-1, -1 , -1):
        if c[j] == "R":
            return j

N = int(input())
c = list(input())

c_set = set(c)
# 全てRは0
if len(c_set) == 1 and c_set == {'R'}:
    print(0)
    sys.exit()

cnt = 0
for i in range(N):
    try:
        first_W = c.index("W")
    except ValueError:
        print(cnt)
        sys.exit()

    last_R = check(c)
    # print(i,':',first_W,', ',last_R)
    
    if first_W < last_R:
        c.pop(first_W)
        c.pop(last_R-1)
        cnt += 1
        continue
print(cnt)

