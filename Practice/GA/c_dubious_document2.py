# https://atcoder.jp/contests/abc076/tasks/abc076_c
import sys
import numpy as np

S_ = np.array(list(input()))
T  = np.array(list(input()))
ans = np.empty(0)
# 文字列Sが存在するかを確かめる
for i in range(len(S_) - len(T)+1):
    for j in range(len(T)):
        if S_[i+j] == '?' or S_[i+j] == T[j]:
            if j == len(T)-1:
                # 文字列Sが存在することが確定
                S = np.concatenate([S_[:i],T],0) # Tと結合させる
                S = ''.join(map(str,S))
                ans = np.append(ans,S.replace('?','a'))
            else:
                # S_の次の文字もTと一致しているかを調べる
                continue
        else:
            break

if len(ans) == 0:
    # 文字列Sが存在しない
    print('UNRESTORABLE')
    sys.exit()
else:
    ans.sort()
    print(ans[0])
