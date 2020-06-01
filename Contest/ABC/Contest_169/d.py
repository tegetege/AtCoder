import math
# 素数判定関数
def isPrime(num):
    # 2未満の数字は素数ではない
    if num < 2: return False
    # 2は素数
    elif num == 2: return True
    # 偶数は素数ではない
    elif num % 2 == 0: return False

    # 3 ~ numまでループし、途中で割り切れる数があるか検索
    # 途中で割り切れる場合は素数ではない
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    # 素数
    return True

# 素数判定
def callIsPrime(input_num=1000):
    prime_num = int()
    number = input_num
    while True:
        if isPrime(number):
            # 素数配列を返す
            return number
        else:
            number += 1

N = int(input())
prime_num = callIsPrime(N/2)
count = 0
target = list()
ans = list()
number = 2
while N != 1:
    prime = callIsPrime(number)
    if N % prime != 0:
        number = prime
        continue # 次の素数に行く
    else:
        e = 1
        while True:
            z = prime ** e
            for i in range(len(target)):
                if z == target[i]:
                    e += 1
                    continue
            target.append(int(prime_num[i] ** e))
            N = int(N/(prime_num[i] ** e))
            ans.append(N)
            count += 1
            break
    numer = 2

# print(ans)
print(count)
