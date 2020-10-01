#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    ll W, a, b;
    cin >> W >> a >> b;
    if (a < b) {
        if (b > a+W) {
            cout << b - (a+W) << "\n";
        } else {
            cout << 0 << "\n";
        }
    } else if (b == a) {
        cout << 0 << "\n";
    } else {
        // b > a の場合
        if (b+W < a) {
            cout << a - (b+W) << "\n";
        } else {
            cout << 0 << "\n";
        }
    }
    
    return 0;
}
