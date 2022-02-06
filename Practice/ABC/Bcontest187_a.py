def cul(target):
    return int(target[0]) + int(target[1]) + int(target[2])


A, B = input().split()
print(max(cul(A), cul(B)))
