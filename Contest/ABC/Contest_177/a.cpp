#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int D, T, S;
    cin >> D >> T >> S;
    if ( D/(S*1.0) <= T) {
        // cout << D/(S*1.0) << endl;
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}
