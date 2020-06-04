#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ans = 0, sum = 0, sub = 0;
    for(int i = 0; i < S.size(); i++) {
        if (S[i] == '+') {
            sum ++;
        } else if (S[i] == '-') {
            sub ++;
        } else {
            continue;
        }
    }
    ans = (sum + 1) - (sub);
    cout << ans << endl;
}
