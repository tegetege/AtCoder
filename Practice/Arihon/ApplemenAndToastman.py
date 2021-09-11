# http://codeforces.com/contest/462/problem/C
"""
操作1
・毎回、Toastmanはグループの数字を得て、全ての数字を足し合わせ、スコアに足すことができる。
・その時、ToastmanはグループをApplemanに渡します

操作2
・毎回、Applemanはグループの中の1つの数字を得て、グループの外に出します。
・Applemanはグループの中から1つ以上の数字を得るたびに、2つの空ではないグループに分けて、
　それぞれをToastmanに渡します。
"""

# listではなくて、heapqueを利用して実装し直す必要がある

N = int(input())
a = list(map(int, input().split()))

a.sort() # インプットを昇順にソート
ans = 0
a_sum = sum(a)
while len(a) > 0:

    ans += a_sum # Toastmanの操作
    b = a.pop(0) # Appleman split操作: 一番小さい数字だけsplitする ここはO(N)
    a_sum -= b
    if len(a) != 0:
        # 最後の1回の時に余分に足されるのを防ぐ
        ans += b # bだけToastmanに渡す

print(ans)
