import sys 
target = list(map(int,input()))

if target[0]+target[1]+target[2]+target[3] == 7:
	print(str(target[0])+'+'+str(target[1])+'+'+str(target[2])+'+'+str(target[3])+'=7')
	sys.exit()
elif target[0]+target[1]+target[2]-target[3] == 7:
	print(str(target[0])+'+'+str(target[1])+'+'+str(target[2])+'-'+str(target[3])+'=7')
	sys.exit()
elif target[0]+target[1]-target[2]+target[3] == 7:
	print(str(target[0])+'+'+str(target[1])+'-'+str(target[2])+'+'+str(target[3])+'=7')
	sys.exit()
elif target[0]+target[1]-target[2]-target[3] == 7:
	print(str(target[0])+'+'+str(target[1])+'-'+str(target[2])+'-'+str(target[3])+'=7')
	sys.exit()
elif target[0]-target[1]+target[2]+target[3] == 7:
	print(str(target[0])+'-'+str(target[1])+'+'+str(target[2])+'+'+str(target[3])+'=7')
	sys.exit()
elif target[0]-target[1]+target[2]-target[3] == 7:
	print(str(target[0])+'-'+str(target[1])+'+'+str(target[2])+'-'+str(target[3])+'=7')
	sys.exit()
elif target[0]-target[1]-target[2]+target[3] == 7:
	print(str(target[0])+'-'+str(target[1])+'-'+str(target[2])+'+'+str(target[3])+'=7')
	sys.exit()
elif target[0]-target[1]-target[2]-target[3] == 7:
	print(str(target[0])+'-'+str(target[1])+'-'+str(target[2])+'-'+str(target[3])+'=7')
	sys.exit()