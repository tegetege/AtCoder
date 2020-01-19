from functools import reduce
import sys
N = list(map(int,input()))
ans = 0
N_int = reduce(lambda a,b:10*a+b, N)


# 1~9の組み合わせ
if 9 <= N_int :
	ans += abs(9 - N[0])
else:
	ans += N
	sys.exit()

# 全ての桁が同じ数での組み合わせ
# Nの一番大きい桁:N[0]
if 11 <= N_int :
	ans += N[0]*(len(N)**2)

# その他の組み合わせ
for i in range(len(N)):
 pass



print(ans)