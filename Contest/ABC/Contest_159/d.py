import math
import copy
N = int(input())
A = list(map(int,input().split()))
A_dict = dict()
for i in range(N):
    if A_dict.get(A[i]) is not None:
        A_dict[A[i]] += 1
    else:
        A_dict[A[i]] = 1

# 各キーが選ばれたときの答えを求めてdict型で持っておく
ans = dict()
for K,V in A_dict.items():
    count = 0
    A_dict_2 = copy.deepcopy(A_dict) # 辞書をオリジナルからコピー,deepcopy
    A_dict_2[K] -= 1 # そのキーを取り出した想定
    for k,v in A_dict_2.items():
        if v >= 2:
            count += int(math.factorial(v)/(2*math.factorial(v-2)))
    ans[K] = count

for i in range(N):
    print(ans[A[i]])
