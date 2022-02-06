def isOK(index, key, a):
    if a[index] >= key:
        return True
    else:
        return False

def binary_search(key, a, N):
    ng = -1
    ok = N

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, key, a):
            ok = mid
        else:
            ng = mid

    return ok

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
C.sort()

# C > B > Aの組み合わせを見つける
# C > B と　B > A の組み合わせの数をカウントしてその積をたす
ans = 0
for i in range(N):
    key = B[i]
    A_index = binary_search(key, A, N)
    C_index = binary_search(key + 1, C, N)
    # print('key: ',key)
    # print('A: ', A[A_index],'   ',A_index)
    # print('C: ', C[C_index],'   ',C_index)

    count_A = A_index
    count_C = N - C_index
    
    ans += count_A * abs(N-C_index)


print(ans)
