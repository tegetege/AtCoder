import itertools
import math

N = int(input())
point = list()
for i in range(N):
	point.append(list(map(int,input().split())))

target = list(itertools.permutations(point))
distance = 0
# 全てのパターンを調べる
for i in range(len(target)):
	# 距離を求める	
	for j in range(len(target[i])-1):
		cul = (target[i][j][0] - target[i][j+1][0])**2 + (target[i][j][1] - target[i][j+1][1])**2
		distance += math.sqrt(cul)
print(distance/len(target))