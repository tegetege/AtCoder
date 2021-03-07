#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    ll X, Y;
    cin >> X >> Y;
    int ans = 0;
    while (X <= Y){
        X *= 2;
        ++ans;
    }
    cout << ans << endl;

    return 0;
}
