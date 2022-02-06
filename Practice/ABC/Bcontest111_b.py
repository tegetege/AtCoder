N = int(input())
ABC_list = [111,222,333,444,555,666,777,888,999]
gap = dict()
for i in ABC_list:
	if i - N >= 0:
		gap[i] = abs(i-N)
print(min(gap))