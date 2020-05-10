import sys
N,M,X = map(int,input().split())
book_list = list()
for i in range(N):
    book_list.append(list(map(int,input().split())))

for i in range(N):
    book_list[i].append(book_list[i][0]/sum(book_list[i][1:M]))
book_list.sort(key=lambda x: x[-1])

dp = [-1 * X]*M

cost = 0
for book in book_list:
    dp_dash = list(map(sum, zip(dp, book[1:M+1])))
    if sum(dp_dash) > sum(dp):
        dp = dp_dash
        cost += book[0]
    if sum(dp) > 0:
        break
    # print(dp_dash)

for i in dp:
    if i < 0 :
        print(-1)
        sys.exit()
print(cost)
