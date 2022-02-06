#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int m, ans;
    cin >> m;

    if (m < 100) {
        cout << "00" << endl;
    } else if (100 <= m and m <= 5000) {
        ans = m / 1000.0 * 10;
        if (ans < 10) {
            cout << "0" << ans << endl;
        } else {
            cout << ans << endl;
        }
    } else if (6000 <= m and m <= 30000) {
        cout << m / 1000 + 50 << endl;
    } else if (35000 <= m and m <= 70000) {
        cout << (m / 1000 - 30) / 5 + 80 << endl;
    } else if (70000 < m) {
        cout << 89 << endl;
    }


    return 0;
}
