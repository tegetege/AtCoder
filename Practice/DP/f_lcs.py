S = list(input())
T = list(input())
s_len = len(S)
t_len = len(T)
# Create array for DP which has over one element.
dp = [[0]*(t_len+1) for i in range(s_len+1)] 

# Get the length of　answer with DP
for i in range(s_len):
    for j in range(t_len):
        if S[i] == T[j]:
            dp[i+1][j+1] = max(dp[i][j+1]+1,dp[i+1][j])
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

# Output
ans = ''
i = s_len
j = t_len
while i > 0 and j > 0:
    if S[i-1] == T[j-1]:
        ans = S[i-1] + ans
        i -= 1
        j -= 1
        # print(ans)
        continue
    if dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1
print(ans)


'''
【Tips】
Python の文字列の長さに対するmax/minを取る方法
>>> max('target1','target2',key = len)
key でlen関数を指定しない場合、Unicodeコードポイント
が大きい方が出力される
>>> max('abcde','efg')
'efg'

https://codom.hatenablog.com/entry/2017/04/20/000000
'''
