N = int(input())
A = list(map(int,input().split()))
A_set = set(A)
print('YES') if len(A) == len(A_set) else print('NO')