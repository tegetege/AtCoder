"""
しゃくとり法
N個の整数を持つ昇順でソートされた配列Aが与えられた場合、
それらの合計がXに等しくなるような要素のペアが存在するかどうか
を調べる.

昇順ソートが行われていないとこれは使えない
"""

import sys
A = list(map(int,input().split()))
X = int(input())

i, j = 0, len(A)-1

while(i < j):
    if (A[i] + A[j]) - X == 0:
        print(True)
        sys.exit()
    elif (A[i] + A[j]) - X < 0:
        i += 1
        continue
    else:
        # (A[i] + A[j]) - X > 0
        j -= 1
        continue

print(False)
