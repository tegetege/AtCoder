N = int(input())
A = list(map(int, input().split()))
A.sort() # 昇順ソート

max_a = A[-1]
ans = [0, 0]
for i in range(2, max_a + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] % i == 0:
            cnt += 1
    if ans[1] < cnt:
        ans[0] = i
        ans[1] = cnt
print(ans[0])
