import sys

K = int(input())
cnt = 1

if K % 2 == 0:
    print(-1)
    sys.exit()

target = 7
i = 0
while True :
    if (cnt >= 2):
        target_1 = '7' * cnt
        target_2 = '7' * (cnt - 1)
        if (cnt == 2):
            target += int(target_1) - 7
        else:
            target += int(target_1) - int(target_2)


    # target_1  = '7' * cnt

    # if (cnt >= 1):
    #     target_1 = '7' * cnt
    #     if (cnt == 1):
    #         target_2 = 0
    #     else:
    #         target_2 = '7' * (cnt - 1)

    #     target += int(target_1) - int(target_2)
    # print(target)


    
    if (target % K == 0):
        print(cnt)
        sys.exit()
    else:
        target = target % K
        cnt += 1
    i+=1
