N = int(input())
L = list()
for i in range(N):
    L_i = int(input())
    L.append(L_i)
long_boad = sum(L)
L.sort(reverse=True)

cost = long_boad
for i in range(N - 2):
    cost += (long_boad - L[0])
    long_boad -= L[0]
    L.pop(0)
    # print('cost ', i + 1, ' : ', cost)

print(cost)
