import math

#素数判定
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

A , B = map(int,input().split())

target = list()
target_max = math.gcd(A,B)

for i in range(1,target_max+1):
	if A % i == 0 and B %i == 0:
		target.append(str(i))


count = 0
if '1' in target :
	count +=1
	target.remove('1')
elif '2' in target:
	count +=1
	target.remove('2')
elif '3' in target:
	count +=1
	target.remove('3')

if len(target) >= 0:
	for i in range(len(target)):
		if  is_prime(int(target[i])):
			count+=1

print(count)