A,B = map(int,input().split())
target = list(range(1,A+1))
target.extend(list(range(1,B+1)))

target.sort(reverse=True)
print(target[0]+target[1])