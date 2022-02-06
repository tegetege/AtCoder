#投げられた文字がACGT文字かどうかを判別
def judge_ACGT(target):
	ACGT = ['A','C','G','T']
	for A in ACGT:
		if str(target) == A:
			return True
	return False

Inp = list(input())
max_count = 0
#リストのすべての文字で検証する
for j in range(len(Inp)):
	count = 0
	match = 1
	for i in range(j,len(Inp)):
		if judge_ACGT(Inp[i]):
			count += 1
			if count >= max_count :
				max_count = count
		else:
			match = 0
			break
	if match == 0:
		continue


print(max_count)