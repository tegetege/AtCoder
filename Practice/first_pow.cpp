#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long n, m, K = 1, ans;
    cin >> m >> n;

    if (n == 0) {
        cout << 1 << endl;
        return 0;
    }
    
    while (n > 1) {
        if (n % 2 != 0) {
            K *= m;
            m = (m * m) % 1000000007;
            n = (n-1) / 2;
        } else {
            m = (m * m) % 1000000007;
            n = n / 2;
        }
    }
    cout << K <<" : "<< m << endl;
    cout << (K * m) % 1000000007 << endl;

    return 0;
}
