# https://leetcode.com/problems/pascals-triangle/
import sys

N = int(input())
ans = list()
    
if N == 1:
    ans.append([1])
    print(ans)
    sys.exit()
if N == 2:
    ans.append([1])
    ans.append([1, 1]) 
    print(ans)
    sys.exit()

ans.append([1])
ans.append([1, 1])
for i in range(2, N):
    print('i:', i)
    target = list()
    target.append(1)
    j = 0
    while j < i - 1:
        print('j: ', j)
        target.append(ans[i - 1][j] + ans[i - 1][j + 1])
        j += 1
    target.append(1)
    ans.append(target)
print(ans)
