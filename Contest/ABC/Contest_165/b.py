import sys
X = int(input())
# X =10 ** 18
x = 100
c = 0
interest = 1.01
while True:
    c += 1
    x = int(x * 1.01)  
    if x >= X:
        print(c)
        sys.exit()
