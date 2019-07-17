N= int(input())
A= list(map(int,input().split()))

Ave = sum(A)/len(A)
abs_distance = list()

for i in range(N):
    abs_distance.append(abs(A[i]-Ave))

print(abs_distance.index(min(abs_distance)))