#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    ll a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << max({a*c, a*d, b*c, b*d}) << "\n";
    return 0;
}
