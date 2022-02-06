N = int(input())
L = list(map(int,input().split()))

L_max = max(L)
L.remove(L_max)

print('Yes') if L_max < sum(L) else print('No')