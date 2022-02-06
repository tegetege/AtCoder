N = int(input())
# 2と1を利用して回答を出力するアルゴリズム
num_2 = int(N / 2)
num_1 = int(N % 2) 
count = num_2 + num_1
# 出力
print(count)
for i in range(num_2):
	print(2)
for i in range(num_1):
	print(1)