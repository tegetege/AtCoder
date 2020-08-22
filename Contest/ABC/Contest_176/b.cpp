#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    string N;
    long long ans=0;
    cin >> N;
    rep(i, N.length()){
        // cout << int(N[i]) - 48 << endl;
        ans += int(N[i]) - 48 ;
    }

    // cout << ans << endl;
    if (ans % 9 == 0 or ans == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
