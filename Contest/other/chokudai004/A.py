import random


N,B_1,B_2,B_3 = map(int,input().split())

l_list   = list()
r_list   = list()
ans_list = list()

#l_listを作成
for i in range(N):
    line = list(map(int,input().split()))
    l_list.append(line)
#r_listを作成
for i in range(N):
    line = list(map(int,input().split()))
    r_list.append(line)


#条件にあうリストの作成
for i in range(N):
    line = list()
    for j in range(N):
        print(random.randint(l_list[i][j],r_list[i][j]),end=' ')
        line.append(random.randint(l_list[i][j],r_list[i][j]))
    ans_list.append(line)
    print('\n')