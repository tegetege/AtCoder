A,B = map(int,input().split())

target = list()

target.append(A+B)
target.append(A-B)
target.append(A*B)

print(max(target))
