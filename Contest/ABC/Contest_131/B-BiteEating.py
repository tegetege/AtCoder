from sys import stdin

class B:
	def __init__(self,N,L):
		self.N = int(N)
		self.L = int(L)
		self.taste = list()
		self.taste_abs = list() #絶対値


	def CollectTaste(self):
		for i in range(1,self.N+1):
			i = self.CulTasteFirst(i)
			self.taste.append(i)
			self.taste_abs.append(abs(i)) #絶対値リストの作成

		#絶対値の小さい要素を削除して計算する味リストの決定
		min_num = min(self.taste_abs)
		try:
			self.taste.remove(min_num)
		except ValueError:
			min_num *= -1
			self.taste.remove(min_num)

		ans = 0
		for i in self.taste:
			ans += i
		print(ans)
	def CulTasteFirst(self,i):
		i = int(i)
		return self.L+i-1


Inp = stdin.readline()
Inp = Inp.replace('\n','')
Inp = Inp.split()

do = B(Inp[0],Inp[1])
do.CollectTaste()

