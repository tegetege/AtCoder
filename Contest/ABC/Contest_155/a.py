number = list(map(int,input().split()))

number_set = set(number)

print('Yes')  if len(number_set) == 2 else print('No')