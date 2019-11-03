S = list(map(int,input()))
count_0 = S.count(0)
count_1 = len(S)-count_0
print(min(count_0,count_1)*2)