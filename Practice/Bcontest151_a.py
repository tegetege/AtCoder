import string
target = list(string.ascii_lowercase)
C = str(input())
print(target[target.index(C)+1])