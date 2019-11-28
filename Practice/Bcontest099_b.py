a,b = map(int,input().split())
gap = abs(a-b)
high = list(range(1,gap))
print(sum(high)-a)