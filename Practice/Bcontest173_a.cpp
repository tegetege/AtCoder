#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, thousand;
    cin >> N;
    thousand = N / 1000;
    if (thousand * 1000 - N == 0) {
        cout << 0 << endl;
    } else {
        cout << (thousand + 1) * 1000 - N << endl;
    }

    return 0;
}
