import sys

N = int(input())
word = list()
for i in range(N):
	word.append(input())

word_set = set(word)
if len(word) != len(word_set): # 同じ単語が使われた時
	print('No')
	sys.exit()

for i in range(N):
	alphabet = list(word[i])
	if i != 0 and last != alphabet[0]:
		print('No')
		sys.exit()	
	last = alphabet[-1]
print('Yes')