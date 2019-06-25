#2人のスタート位置の差が奇数の時はAliceの勝ち
#偶数の時はBorysの勝ち
#2人のスタート位置の差が0の時はBorysの勝ち

N, A, B= map(int, input().split())
if (abs(A-B)-1) % 2 == 1: print('Alice')  
else: print('Borys') 
