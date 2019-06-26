'''
入力された数字をソートして、
前から2つずつの組みにして、その２つの小さい方を
足していく
'''

N = input() 
Inp = list(input().split())
Inp = [int(i) for i in Inp]
Inp.sort()
ans = 0
for i in range(0,len(Inp),2) :
	kushi = [int(Inp[i]),int(Inp[i+1])]
	ans += min(kushi)
print(ans)