N,D = map(int,input().split())
print(int(N/((D*2)+1))+1) if int(N % ((D*2)+1)) != 0 else print(int(N/((D*2)+1)))