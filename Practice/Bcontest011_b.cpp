#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    string S;
    cin >> S;
    rep(i, S.size()) {
        if (i==0) {
            S[i] = toupper(S[i]);
        } else {
            S[i] = tolower(S[i]);
        }
    }
    cout << S << "\n";
    return 0;
}
