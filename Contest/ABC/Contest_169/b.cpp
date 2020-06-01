#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    long long ans,line, line_half;
    ans = 1;
    line = 1000000000000000000;
    line_half = 1000000000;
    // 入力
    rep(i,N) {
        cin >> A.at(i);
    }

    // 0処理
    rep(i,N) {
        if (A.at(i) == 0) {
            cout << "0" << endl;
            exit(0);
        }
    }

    // 答えを求める
    rep(i,N) {
        // cout << ans << " : " << A.at(i) << endl;
        if (ans >= line_half && A.at(i) >= line_half) {
            cout << "-1" << endl;
            exit(0);
        } else {
            ans *= A.at(i);
        }
        if (ans > line) {
            cout << "-1" << endl;
            exit(0);
        }
    }
    cout << ans << endl;
}
