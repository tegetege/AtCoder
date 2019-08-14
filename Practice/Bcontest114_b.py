S = list(map(str,input()))
gap =1000 #初期gap、最大753

for i in range(len(S)-2):
    target=S[int(i):int(i)+3]#ターゲットの切り出し
    # print('target:',target)
    # print(abs(753 - int(''.join(target))))
    if gap > abs(753 - int(''.join(target))):
        gap = abs(753 - int(''.join(target)))

print(gap)