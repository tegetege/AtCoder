'''
(1)3つのパッケージから一番大きなパッケージを見つける
(2)残りの2つのパッケージの和が(1)のパッケージと同じ値ならYes、
　　異なる場合は'No'
'''

a, b, c= map(int, input().split())

Inp = [a,b,c]
Sum = 0
max_num = max(Inp)
Inp.remove(max_num)
for i in Inp: Sum += i
if max_num == Sum: print('Yes') 
else: print('No')