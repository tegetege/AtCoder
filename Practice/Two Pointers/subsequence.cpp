// Subsequence POL No.3061
// 蟻本 P.135

#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int n, S;
    cin >> n;
    cin >> S;
    vector<int> a(n);
    rep(i, n) {
        cin >> a.at(i);
    }

    int ans = n + 1; // 上界

    int right = 0;
    long long sum = 0;
    for (int left = 0; left < n; ++left) {
        while (left < n && sum < S) {
            sum += a[left];
            ++left;
        }
        if (sum < S) break;
        ans = min(ans, right - left);

        // for文でleftがインクリメントされる準備
        if (right == left) {
            // right == leftの場合、そのまま区間が右にずれるので、
            // rightもインクリメントする
            ++right;
        } else {
            // left のみがインクリメントする場合は、
            // インクリメントで外れてしまうleftの区間の値を引く
            sum -= a[left];
        }
    }

    if (ans < n+1) {
        cout << ans << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
