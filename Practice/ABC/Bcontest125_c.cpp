#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

long long GCD(long long a, long long b) {
    if (a % b == 0) {
        return b;
    } else {
        return GCD(b, a%b);
    }
}

template<class T> inline bool chmax(T& a, T b) {
    if (a < b) {
        a = b;
        return 1;
    } 
    return 0;
}

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    rep(i, N){
        cin >> A[i];
    }

    vector<long long> left(N+1, 0), right(N+1, 0);
    for (int i = 0; i < N; ++i) {
        left[i+1] = GCD(left[i], A[i]);
    }
    for (int i = N-1; i >= 0; --i) {
        right[i] = GCD(right[i+1], A[i]);
    }

    long long ans = 0;
    rep(i, N) {
        long long l = left[i];

        long long r = right[i+1];
        
        long long g = GCD(l, r);
        cout << g << ": gcd" << endl; 
        ans = max(ans, g);
        cout << i << " 終了" << endl;
    }

    cout << ans << endl;

    return 0;
}
