#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, K, ans = 0;
    cin >> N >> K;
    vector<int> p(N);
    rep(i,N) {
        cin >> p[i];
    }
    sort(p.begin(), p.end());

    rep(i,K) {
        ans += p[i];
    }
    cout << ans << endl;

    return 0;
}
