#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    ll N, M, K;
    cin >> N >> M >> K;
    vector<ll> A(N), B(M);
    rep(i, N) {
        cin >> A.at(i);
    }
    rep(i, M) {
        cin >> B.at(i);
    }

    ll t = 0;
    rep(i, M) t += B[i];

    int j = M;
    int ans = 0;
    // Aを一冊づつ進めていき、Bが何冊読めるのか進めていく
    // しゃくとり法
    rep(i, N+1) {
        // 合計時間tがKを超えている場合Bの一冊を諦める
        while (j > 0 && t > K) {
            --j;
            t -= B[j];
        }
        if (t > K) break;
        ans = max(ans, i+j); // 読める最大数
        if (i == N) break;
        t += A[i]; // 次のループではAの一冊を含めている状態にする
    }
    cout << ans << "\n";
    return 0;
}
