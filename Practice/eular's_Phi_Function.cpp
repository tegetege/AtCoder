// http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_D&lang=ja

#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

vector<pair<long long, long long> > prime_factorize(long long N) {
    vector<pair<long long, long long> > res;
    for (long long i = 2; i * i <= N; ++i) {
        if (N % i != 0) {
            continue; 
        }
        long long ex = 0; // 指数
        // 割れるだけ割る
        while (N % i == 0) {
            ++ex;
            N /= i;
        }
        // 結果を push
        res.push_back({i, ex});
    }

    // 残った数はそのまま push
    if (N != 1) {
        res.push_back({N, 1});
    }

    return res;
}

int main() {
    long long N;
    cin >> N;

    const auto &res = prime_factorize(N); // 素因数分解
    long long ans = N;
    for (auto p : res) {
        ans *= (p.first - 1);
        ans /= p.first;
    }
    cout << ans << endl;

    return 0;
}

