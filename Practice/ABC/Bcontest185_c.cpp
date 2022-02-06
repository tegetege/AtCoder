#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int L;
    cin >> L;
    ll ans = 1;
    for(int i = 1; i <= 11; ++i) {
        ans *= L-i;
        ans /= i;
    }
    cout << ans << endl;
    return 0;
}
