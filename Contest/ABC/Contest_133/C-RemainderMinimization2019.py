'''
TLE でAC できなかった
'''

import itertools
L , R  = map(int,input().split())
num_list = list(range(L,R+1))
mod = list()
for j in itertools.combinations_with_replacement(num_list,2):
	mod.append((j[0]*j[1])%2019)
print(min(mod))