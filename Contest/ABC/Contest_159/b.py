import sys
S = list(input())
N = len(S)
S_r = list(reversed(S))
if S == S_r:
    # (N-1)/2を抜き出す
    S_2 = S[:int((N-1)/2)]
    S_2_r = list(reversed(S_2))
    if S_2 == S_2_r:
        S_3 = S[int((N+3/2)):N]
        S_3_r = list(reversed(S_3))
        if S_3 == S_3_r:
            print('Yes')
            sys.exit()
print('No')

