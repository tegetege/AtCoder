from collections import defaultdict
n, m = [int(i) for i in input().split()]
h = [0] + list(map(int, input().split()))

peak = defaultdict(list)

for _ in range(m):
    p1, p2 = list(map(int, input().split()))
    peak[p1].append(p2)
    peak[p2].append(p1)
    
# print(peak)

cnt = 0
for k, roads in peak.items():
    total = len(roads)
    
    subtotal = 0 # kより高さが低い展望台の数
    for road in roads:
        if h[road] < h[k]:
            subtotal += 1

    if subtotal == total:
        cnt += 1
    
cnt += n - len(peak)
print(cnt)
