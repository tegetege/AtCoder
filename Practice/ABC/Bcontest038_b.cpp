#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int H_1, H_2, W_1, W_2;
    cin >> H_1 >> W_1;
    cin >> H_2 >> W_2;

    if (H_1 == H_2 or W_1 == H_2 or H_1 == W_2 or W_1 == W_2) {
        cout << "YES" << endl;
        return 0;
    } else {
        cout << "NO" << endl;
        return 0;
    }

    return 0;
}
