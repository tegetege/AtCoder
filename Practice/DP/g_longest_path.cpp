#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < (n); i++)
// 隣接リスト グラフ, 可変長配列
vector<int> to[100005];
int dp[100005];


int DP(int i) {
    if (dp[i] != -1) {
        return dp[i];
    }

    int tmp = 0;
    for(auto e : to[i]) {
        tmp = max(tmp, DP(e) + 1);
    }
    dp[i] = tmp;
    return tmp;
}


int main(void){
    int N, M;
    cin >> N >> M;
    rep(i, M) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        to[x].push_back(y);
    }
    // dp初期化
    rep(i, 100005) {
        dp[i] = -1;
    }


    // 出力
    int ans = 0;
    rep(i, N){
        ans = max(ans, DP(i));
    }
    cout << ans << endl;

    return 0;
}
