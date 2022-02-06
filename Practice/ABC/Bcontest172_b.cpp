#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S, T;
    cin >> S;
    cin >> T;
    int count = 0;
    rep(i, S.size()) {
        if (S[i] != T[i]) {
            ++count;
        }
    }
    cout << count << endl;

    return 0;
}
