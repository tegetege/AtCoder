#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int N, W;
    cin >> N >> W;

    ll w[N], v[N];
    for(int i = 0; i < N; i++) {
        cin >> w[i] >> v[i];
    }

    ll INF = 1e9+1;
    ll max_v = 1000 * 100;
    ll dp[max_v + 1];

    // dp[i]: 価値iを作れる時の重さの最小値
    // 最小値を得たいので、INFをあらかじめ代入
    for(int i = 0; i < max_v + 1; i++){
        dp[i] = INF;
    }
    
    // dpの要素番号 = 価値
    dp[0] = 0;
    for(int i = 1; i <= N; i++){
        for(int j = max_v; j >= 0; j--){
            if(j - v[i-1] >= 0){
                dp[j] = min(dp[j], dp[j-v[i-1]] + w[i-1]);
            }
        }
    }

    ll ans = 0;
    for(int i = 0; i <= max_v; i++){
        if(dp[i] <= W){
            // dpに格納したウェイトがW以下の場合、その要素番号と
            // ansのくらいを比較する
            ans = max(ans, (ll)i);
        }
    }

    cout << ans << endl;
}
