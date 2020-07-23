#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long N, P, ans = 1;
    cin >> N >> P;

    vector<pair<long long, long long> > ress;

    for(long long i = 2; i * i <= P; ++i) {
        if (P % i != 0) {
            continue;
        }

        long long ex = 0; // 指数
        while (P % i == 0) {
            ++ex;
            P /= i;
        }
        // 結果を保存
        ress.push_back({i, ex});
    }
    // 残った数字の処理
    if (P != 0) {
        ress.push_back({P, 1});
    }

    // 各素因数の指数を均等にN個に分ける(int/int = int)
    for (pair<long long, long long> res : ress) {
        if (res.second >= N ) {
            ans *= pow(res.first, (res.second / N));
        }
    }
    cout << ans << endl;
    return 0;
}
