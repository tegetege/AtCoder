import string
import sys
A = list(input())

ans = list()
ascii_lowercase = list(string.ascii_lowercase)

if A[-1] != 'a':
# 最後がaではない場合
    A[-1] = ascii_lowercase[ascii_lowercase.index(A[-1])-1]
else:
    # 最後がaの場合
    if len(A) == 1:
        print('-1')
        sys.exit()
    else:
        print(A.pop())
        sys.exit()

print(''.join(A))
