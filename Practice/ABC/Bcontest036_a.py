A,B = map(int,input().split())

print(int(B/A)+1) if B % A != 0 else print(int(B/A))