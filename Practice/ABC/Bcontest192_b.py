s = list(input())

for i in range(len(s)):
    #偶数で小文字
    if (i + 1) % 2 == 0 and s[i].islower():
        print('No')
        exit()
    #奇数で大文字
    if (i + 1) % 2 != 0 and s[i].isupper():
        print('No')
        exit()

print('Yes')