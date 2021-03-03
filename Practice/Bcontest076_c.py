import copy


def ans(S_, T):
    for i in range(len(S_) - len(T), -1, -1):
        if isContainString(S_, T, i):
            tmp = copy.deepcopy(S_)
            for j in range(len(T)):
                tmp[i + j] = T[j]
            return ''.join(list(map(lambda v: v.replace('?', 'a'), tmp)))
    return 'UNRESTORABLE'


def isContainString(S_, T, index):
    for j in range(len(T)):
        S_char = S_[index + j]
        Tchar = T[j]

        if S_char != '?' and Tchar != S_char:
            return False
    return True


if __name__ == '__main__':
    S_ = list(input())
    T = list(input())
    print(ans(S_, T))


# 辞書順最小のために後ろから考える
# status = 0
# len_T = len(T)
# for i in range(len(S_) - 1, -1, -1):
#     if (S_[i] == '?' or S_[i] == T[-1]) and len_T <= abs(i + 1):
#         j = len(T) - 1
#         i_ = copy.deepcopy(i)
#         while j >= 0 and i_ >= 0:
#             if S_[i_] == '?':
#                 status = 1
#             elif S_[i_] == T[j]:
#                 status = 1
#             else:
#                 status = 0
#                 break
#             i_ -= 1
#             j -= 1
#     else:
#         print('UNRESTORABLE')
#         sys.exit()
#     if status == 1:
#         for cnt in range(len(T) - 1, -1, -1):
#             S_[i] = T[cnt]
#             i -= 1
#         ans = list(map(lambda v: v.replace('?', 'a'), S_))
#         print(''.join(ans))
#         sys.exit()
# print('UNRESTORABLE')
