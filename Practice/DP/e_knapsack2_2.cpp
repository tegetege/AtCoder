#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    ll N, W;
    cin >> N >> W;

    ll INF = 1e9+1;
    int MAX_VALUE = 1000*100;
    vector<ll> w(N), v(N), DP(MAX_VALUE+1, INF);
    rep(i, N) {
        cin >> w.at(i) >> v.at(i);
    }

    DP[0] = 0;
    for(int i = 0; i < N; ++i) {
        for(int j = MAX_VALUE; j >= 0; --j) {
            if (j - v[i] >= 0) {
                DP[j] = min(DP[j], DP[j-v[i]]+w[i]); // もらうDP
            }
        }
    }

    int ans = 0;
    for(int i = 0; i < MAX_VALUE; ++i) {
        if (DP[i] <= W) {
            ans = max(ans, i);
        }
    }
    cout << ans << endl;
    return 0;
}
