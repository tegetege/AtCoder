#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    string S,T;
    cin >> S;
    cin >> T;
    int count = 0, ans = 100000;
    for(int i = 0; i <= S.length() - T.length(); ++i) {
        count = 0;
        for(int j = 0; j < T.length(); ++j) {
            if (S[i+j] != T[j]) {
                ++count;
            }
        }
        ans = min(ans, count);
    }
    cout << ans << endl;
    return 0;
}
