'''
Dについてのinputのみを利用する
Dについてのinputをソートして、その
D[int(len(D)/2)]とD[int(len(D)/2)-1]の差を求める

'''

N = input()
D = [int(i) for i in list(input().split())]
D.sort()
print(int(D[int(len(D)/2)])-int(D[int(len(D)/2)-1]))
# print('D/2:',int(D[int(len(D)/2)-1]))
# print('D/2+1:',int(D[int(len(D)/2)]))
# print('gap:',int(D[int(len(D)/2)])-int(D[int(len(D)/2)-1]))

