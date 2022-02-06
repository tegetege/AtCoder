N,X = map(int,input().split())
L = list(map(int,input().split()))
D = [0]
for i in range(len(L)):
	if D[i]+L[i] <= X:
		D.append(D[i]+L[i])
	else:
		break

print(len(D))