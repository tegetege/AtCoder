class Get_set_num:
	def __init__(self):
		self.num = int()
		 
	def set_num(self,num):
		self.num = num

	def get_num(self):
		return self.num

		 
do  = Get_set_num()
Inp = input()
Inp = int(Inp)


#割れる回数が最大の数とその回数を記録するリスト
#max[0]が対象となる数、max[1]が割れた回数
max_list = [1,0]

for i in range(Inp , 1 , -1):
	count=0
	do.set_num(i)
	while i % 2 == 0:
		count += 1
		i= i/2
		if count > max_list[1]:
			max_list.clear()
			max_list.extend([do.get_num(),count])
			
print(max_list[0])