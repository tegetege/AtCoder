#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, min = 1001, max = -1, a;
    cin >> N;
    rep(i, N) {
        cin >> a;
        if (a < min) {
            min = a;
        } 
        if (a > max) {
            max = a;
        }
    }
    cout << max - min << endl;

    return 0;
}
