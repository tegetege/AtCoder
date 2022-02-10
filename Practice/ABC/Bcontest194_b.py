n = int(input())
a_list = list()
b_list = list()

for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

res = 1000000000
for i in range(n):
    for j in range(n):
        target = a[i] + b[i] if i == j else max(a[i], b[i])
        res = min(res, target)
