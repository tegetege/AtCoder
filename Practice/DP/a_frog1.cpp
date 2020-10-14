#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 1; i <= (int)(n); i++)

int main() { 
    ll N, inf = 10000007777;
    cin >> N;
    vector<ll> h(N+1), DP(N+1, inf);
    rep(i, N) {
        cin >> h.at(i);
    }

    DP[1] = 0;
    DP[2] = abs(h[2] - h[1]);
    for(int i = 3; i <= N; ++i) {
        DP[i] = min(DP[i-1] + abs(h[i]-h[i-1]), DP[i-2] + abs(h[i]-h[i-2]));
    }
    cout << DP[N] << "\n";

    return 0;
}
