from sys import stdin



class C:
	def __init__(self,A,B,C,D):
		self.A = int(A)
		self.B = int(B)
		self.C = int(C)
		self.D = int(D)
		self.count = 0

	def main(self):
		for i in range(self.A,self.B+1):
			if i % self.C != 0:
				if  i % self.D != 0:
					self.count +=1
		print(self.count)


Inp = stdin.readline()
Inp = Inp.replace('\n','')
Inp = Inp.split()

do = C(Inp[0],Inp[1],Inp[2],Inp[3])

do.main()
