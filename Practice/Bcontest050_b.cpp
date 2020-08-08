#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, M, P, X;
    long long ans=0, gap;

    cin >> N;
    vector<long long> T(N), ANSER(N);
    rep(i, N){
        cin >> T.at(i);
        ans += T[i];
    }

    cin >> M;
    rep(i, M) {
        cin >> P >> X;
        gap = T[P-1] - X;
        ANSER.at(i) = ans - gap;
    }

    rep(i, M) {
        cout << ANSER[i] << endl;
    }


    return 0;
}
