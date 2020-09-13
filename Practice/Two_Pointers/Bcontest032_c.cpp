#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    ll N, K, ans_len = 0, right = 0, target=1;
    cin >> N >> K;

    vector<ll> s(N);
    rep(i, N) {
        cin >> s.at(i);
    }

    // 入力に0がある場合は N を出力
    rep(i, N) {
        if (s[i] == 0) {
            cout << N << endl;
            return 0;
        }
    }


    for (ll left = 0; left < N; ++left) {
        while (right < N && target * s[right] <= K) {
            target *= s[right];
            ++right;
        }

        ans_len = max(ans_len, right - left);
        if (left == right) {
            ++right;
        } else {
            target /= s[left];
        }
        
    }

    cout << ans_len <<"\n";
    return 0;
}
