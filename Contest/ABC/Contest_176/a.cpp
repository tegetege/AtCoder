#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int N, X, T;
    cin >> N >> X >> T;
    if (N % X != 0) {
        cout << T * ((N/X)+1) << endl;
    } else {
        cout << T * (N/X) << endl;
    }

    return 0;
}
