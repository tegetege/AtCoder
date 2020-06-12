#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, l, r, ans = 0;
    cin >> N;
    rep(i, N) {
        cin >> l >> r;
        ans += abs(l-r) + 1;
    }
    cout << ans << endl;

    return 0;
}
