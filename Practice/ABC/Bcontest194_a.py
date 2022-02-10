a, b = map(int, input().split())

if (a+b >= 15 and b >= 8):
    print(1)
    exit()
if (a+b >= 10 and b >= 3):
    print(2)
    exit()
if (a+b >= 3):
    print(3)
    exit()

print(4)