# 再帰関数で計算
import sys

def caracal(H,count,separate_number):
	if H == 1:
		return count
	else:
		H = int(H/2)
		count = count + (separate_number*2)
		# 攻撃時の分離数
		separate_number = separate_number * 2 
	return caracal(H,count,separate_number)




H = int(input())
print(caracal(H,1,1))