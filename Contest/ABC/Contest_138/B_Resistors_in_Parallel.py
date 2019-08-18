N = int(input())
A = list(map(int,input().split()))

denominator = int()

for i in A:
	denominator += 1/i

print(1/denominator) 