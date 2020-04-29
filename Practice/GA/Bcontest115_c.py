N,K = map(int,input().split())
H_input = list()
ABS = float('inf')

for i in range(N):
    H_input.append(int(input()))
H_input.sort()

# print(H_input)
for i in range(N-K+1):
    # print(H_input[i:(i+K)])
    if ABS > (H_input[i+K-1] - H_input[i]):
        # print('Before:',ABS)
        ABS = H_input[i+K-1] - H_input[i]
        # print('After:',ABS)
print(ABS)
