Inp = input()
Inp_list = list(Inp) 

F_x = 0
for i in Inp_list: F_x += int(i)

if int(Inp) % F_x == 0: print('Yes')
else: print('No') 