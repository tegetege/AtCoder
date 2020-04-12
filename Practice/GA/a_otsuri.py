# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a

otsuri = 1000 - int(input())
ans = 0 # お釣りの枚数
coin_list = [500,100,50,10,5,1]
for coin in coin_list:
  if otsuri / coin >= 1:
    # print(coin,':',int(otsuri / coin))
    ans += int(otsuri / coin)
    otsuri -= coin * int(otsuri / coin)
print(ans)
