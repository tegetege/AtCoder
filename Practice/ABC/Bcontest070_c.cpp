#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

long long gcd(long long a, long long b) {
    // 再帰を利用
    // if (a%b == 0) {
    //     return b;
    // } else {
    //     return gcd(b, a%b);
    // }

    // while文を利用
    long long b_;
    while (b != 0) {
        b_ = b;
        b = a % b;
        a = b_;
        // cout << a << ":" << b << endl;
    }
    return a;
}

long long lcm(long long a, long long b) {
    // cout << gcd(a, b) << endl;
    return (a / gcd(a, b)) * b;
}


int main() {
    int N;
    cin >> N;
    vector<long long> T(N);

    rep(i, N) {
        cin >> T.at(i);
    }

    long long ans = T[0];
    for (int i = 1; i < N; ++i) {
        ans = lcm(ans, T[i]);
    }
    cout << ans << endl;
    
    return 0;
}
