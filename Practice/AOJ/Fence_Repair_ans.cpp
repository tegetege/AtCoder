#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    // 入力
    ll N, ans = 0;
    cin >> N;
    vector<ll> L(N);
    rep(i, N) {
        cin >> L[i];
    }
    // 順位キューの準備(小さい数から出てくるように設定)
    priority_queue<int, vector<int>, greater<int>> que;
    rep(i, N) {
        que.push(L[i]);
    }
    while(que.size() > 1) {
        int l1, l2;
        l1 = que.top(); que.pop();
        l2 = que.top(); que.pop();
        ans += l1 + l2;
        que.push(l1 + l2);
    }

    cout << ans << endl;

    return 0;
}
