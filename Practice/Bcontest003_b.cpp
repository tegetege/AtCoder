#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string S, T, target;
    cin >> S ;
    cin >> T ;
    target = "atcoder";
    rep(i, S.size()) {
        if (S[i] == '@' && T[i] == '@' || S[i] == T[i]) {
            continue;
        } else if (S[i] == '@' || T[i] == '@') {
            if (S[i] == '@' && target.find(T[i]) != string::npos) {
                continue;
            } else if (T[i] == '@' && target.find(S[i]) != string::npos) {
                continue;
            } else {
                cout << "You will lose" << endl;
                exit(0);
            }

        } else {
            cout << "You will lose" << endl;
            exit(0);
        }
    }
    // cout << target.find("a") << endl;
    // cout << typeid(target.find("i")).name() << endl;
    cout << "You can win" << endl;
}
