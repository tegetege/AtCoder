import numpy as np
N,M = map(int,input().split())
homeworks = np.asarray(list(map(int,input().split())))
homeworks = np.sum(homeworks)
print(N-homeworks) if N >= homeworks else print('-1')
