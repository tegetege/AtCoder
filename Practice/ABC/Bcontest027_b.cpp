#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int N, p=0; // p: 住人の数
    cin >> N;
    vector<int> a(N);
    set<int> s;
    rep(i, N) {
        cin >> a[i];
        p += a[i];
        s.insert(a[i]);
    }
    if (s.size() == 1) { // 全ての島の人数が同じ場合
        cout << 0 << endl;
        return 0;
    }

    if (p % N != 0) { // 実現できないパターン
        cout << -1 << endl;
        return 0;
    }
    
    int ave= p / N; // 1つの島に住む人数
    int cnt = 0, sum = 0, ans = 0;
    rep(i, N) {
        sum += a[i];
        ++cnt;
        if (sum == ave * cnt) {
            sum = 0;
            cnt = 0;
            continue;
        }
        ++ans;
    }
    cout << ans << endl;
    return 0;
}
