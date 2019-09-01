'''
i  : 1 2 3 4 5 6 7 8 9  10
のとき、P_iを
P_i: 2 3 4 5 6 7 8 9 10 1

iが１~ N-1までは等差数列の和の公式で
求められる
最後の項目は0である

'''

N = int(input())
target = int(((N-1)*(2+N-2))/2)

target += N % 1
print(target)
# N_list.reverse()

# N_list.pop(-1)
# print(N_list)