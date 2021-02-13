// http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int n, m;
    cin >> n >> m;
    vector<int> c(m), dp(n+1, 50001);
    rep(i, m) {
        cin >> c.at(i);
    }
    
    dp[0] = 0;
    for(int i = 0; i <= n; ++i) {
        rep(j, m) {
            if (i - c[j] < 0) break;
            dp[i] = min(dp[i], dp[i - c[j]] + 1);
        }
    }

    for(auto e: dp) {
        cout << e << " ";
    } cout << endl;

    cout << dp[n] << endl;
    return 0;
}
