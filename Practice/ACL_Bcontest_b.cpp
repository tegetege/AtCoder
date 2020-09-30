#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    ll A, B, C, D;
    cin >> A >> B >> C >> D;
    if (B < C or D < A) {
        cout << "No" << "\n";
    } else {
        cout << "Yes" << "\n";
    }
    return 0;
}
