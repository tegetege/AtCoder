K = int(input())
#奇数
odd  = list(range(1,K+1,2))
#偶数
even = list(range(2,K+1,2))
print(len(odd)*len(even))