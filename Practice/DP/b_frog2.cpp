#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 1; i <= (int)(n); i++)
#define endl "\n"

int main() { 
    ll N, K;
    cin >> N >> K;
    // 1~N+1 で考える
    vector<ll> h(N+1), dp(N+1, 10000007777);
    rep(i, N) {
        // 1から開始する
        cin >> h.at(i);
    }

    dp[1] = 0;
    for(ll i = 1; i <= N; ++ i) {
        for(ll j = i; j <= min(i+K, N); ++j) {
            dp[j] = min(dp[j], dp[i]+abs(h[j]-h[i]));
        }
        // cout << "i: " << i << "j+k: " << i+K << endl; 
        // for(const auto& e: dp) {
        // cout << e << " ";
        // } cout << endl;
    }
    

    cout << dp[N] << endl;
    return 0;
}
