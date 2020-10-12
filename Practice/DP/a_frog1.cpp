#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 1; i <= (int)(n); i++)

int main() { 
    ll N, inf = 10000007;
    cin >> N;
    vector<int> h(N+1), DP(N+1, inf);
    rep(i, N) {
        cin >> h.at(i);
    }

    DP[1] = 0;
    for(int i = 2; i <= N; ++i) {
        DP[i] = min(DP[i], DP[i-1] + abs(h[i]-h[i-1]));
        if (i >= 3) {
            DP[i] = min(DP[i], DP[i-2] + abs(h[i]-h[i-2]));
        }
        // cout << DP[i] << "\n";
    }
    cout << DP[N] << "\n";

    return 0;
}
