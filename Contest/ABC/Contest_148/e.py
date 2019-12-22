# import sys
# sys.setrecursionlimit(10**5+10)

N = int(input())

def f(N):
	if N < 2:
		return 1
	else:
		return N * f(N-2)

ans = f(N)
# ans_list = list(str(ans))
# print(ans_list)
print(ans)