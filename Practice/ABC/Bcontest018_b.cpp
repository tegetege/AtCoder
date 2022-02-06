#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S, S_t;
    int N,l,r;
    cin >> S;
    cin >> N;
    rep(i, N) {
        cin >> l >> r;
        S_t = S;
        for(int j = 0; j < (r - l + 1); ++j) {
            S[l - 1 + j] = S_t[r - 1 - j];
        }
    }

    cout << S << endl;
    return 0;
}
