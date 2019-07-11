#最小公倍数を求めるgcd()はmath.gcd()もあるが、
#Atcoderのバージョン関係で、fractions.gcd()を利用する

#A / C → 0~Aに含まれるCの割り切れる個数
#全体の対象の数-(Cで割り切れる個数+Dで割り切れる個数-CとDの最小公倍数で割り切れる数)

import fractions

A,B,C,D = map(int, input().split())


c_and_d=C*D
#CとDの最小公倍数を求める
lcm = int(C*D//fractions.gcd(C,D))


count_C =0
count_D =0
count_C_and_D =0

count_C = int(B//C)-int((A-1)//C)
count_D = int(B//D)-int((A-1)//D)
count_C_and_D = int(B//lcm)-int((A-1)//lcm)

print(int((B-A+1) -(count_C + count_D - count_C_and_D)))