N,A,B = map(int,input().split())

set_count  = int(N/(A+B))
if  N % (A+B) != 0:
    ans = set_count * A
    last_ball = N - (A+B)*set_count
    if last_ball <= A:
        ans += last_ball
    else:
        ans += A
else:
    ans = set_count * A
print(ans)