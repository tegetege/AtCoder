#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int N, ans = 0;
    ll now = -1000000001;
    cin >> N;
    vector<pair<int, int>> arm;

    rep(i, N){
        ll x, l;
        cin >> x >> l;
        // ソートしたいので、(右腕, 左腕)の形式で入力
        arm.push_back(make_pair(x + l, x -l));
    }
    sort(arm.begin(), arm.end()); // 右腕を基準にソート

    rep(i, N) {
        if (arm[i].second >= now) {
            ++ans;
            now = arm[i].first;
        }
    }

    cout << ans << endl;
    return 0;
}
