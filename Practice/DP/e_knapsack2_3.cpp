#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() {
    ll N, W, line;
    ll INF = 1e9+1;
    int MAX_VALUE = 1000*100+1;
    cin >> N >> W;

    vector<vector<ll>> DP(N+1, vector<ll>(MAX_VALUE+1, INF));
    vector<ll> w(N), v(N);
    rep(i, N) {
        cin >> w[i] >> v[i];
    }

    DP[0][0] = 0;
    for(int i=0; i < N; ++i) {
        for(int j=0; j <= MAX_VALUE; ++j) {
            if (j < v[i]) {
                DP[i+1][j] = DP[i][j];
            } else {
                DP[i+1][j] = min(DP[i][j], DP[i][j-v[i]]+w[i]);
            }
        }
    }

    int ans = 0;
    for(int i = 0; i < MAX_VALUE; ++i) {
        if (DP[N][i] <= W) {
            ans = i;
        }
    }
    cout << ans << endl;
    return 0;
}
