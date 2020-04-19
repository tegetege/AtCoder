import numpy as np

N = int(input())
A = np.asarray(list(map(int,input().split())))
A_sort = np.sort(A)
# print(A_sort)
k = 0
for i in range(1,N+1):
    count = 0
    for j in range(k,N-1):
        if A_sort[j] == i:
            count += 1
        else:
            break
    print(count)
    k += count
