N = int(input())
ANS = 10**10 + 2
i = 1
while i * i <= N:
    if (N % i == 0):
        # print(i,' : ', int(N / i))
        max_len = max(len(str(i)),len(str(int(N / i))))
        ANS = min(ANS, max_len)

    i += 1

print(ANS)
