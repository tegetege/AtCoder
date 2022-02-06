#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long N, M;
    cin >> N >> M;

    // 素因数分解
    vector<pair<long long, long long> > ress;
    for (long long i = 2; i * i <= M; ++i) {
        if (M % i != 0) {
            continue;
        }

        long long ex = 0; // 指数
        while(M % i == 0) {
            ++ex;
            M /= i;
        }
        // 結果をpush
        ress.push_back({i, ex});
    }

    // 残った数字はそのままpush
    if (M != 1) {
        ress.push_back({M, 1});
    }

    long long ans = 1, right = 1;
    // (N-1)!を求める
    for (long long i = 0; i < (N-1); ++i) {
        right *= (N-1)-i;
    }


    for (pair<long long, long long> res : ress) {
        // cout << res.first << ":" << res.second << endl;
        // 重複組み合わせ
        // e個の素因数をN個に分ける
        // H(N,e) = C(e+N-1,N-1)
        unsigned long long left = 1;
        for(long long j = 0; j < (N-1);++j ){
            left *= (res.second + (N-1) - j);
        }
        cout << left << ":" << right << ":" << ans << endl;
        ans *= left / right;

        ans %= 1000000007;
        
    }
    cout << ans << endl;

    return 0;
}
