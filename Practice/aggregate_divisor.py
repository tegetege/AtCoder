N = int(input())
ANS = set()
i = 2
while i * i <= N:
    if (N % i == 0):
        ANS.add(i)
        ANS.add(int(N / i))
    i += 1
ANS.add(N) # N自身も約数なので追加

print(ANS)
