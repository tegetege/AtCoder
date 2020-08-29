#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    long long N, a, mod = 1000000007, ans = 0, sum_all = 0;
    cin >> N;
    vector<long long> A(N);
    rep(i, N) {
        cin >> a;
        A[i] = a % mod;
        sum_all += a % mod;
    }

    for(long long i = 0; i < N-1; ++i) {
        sum_all -= A[i];
        // cout << sum_all << " : " << A[i] << endl; 
        ans = (ans + ((A[i] * sum_all) % mod)) % mod;
    }
    cout << ans << endl;

    return 0;
}
