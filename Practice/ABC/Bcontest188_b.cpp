#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int N;
    cin >> N;
    vector<int> A(N, 1), B(N, 1);

    rep(i, N){
        cin >> A[i];
    }
    rep(i, N){
        cin >> B[i];
    }

    ll ans=0;
    rep(i, N) {
        ans += A[i] * B[i];
    }
    if (ans == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
