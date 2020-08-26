#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    vector<vector<string>> c(4, vector<string>(4));
    for(int i = 3; i >= 0; --i) {
        for(int j = 3; j >= 0; --j) {
            cin >> c.at(i).at(j);
        } 
    }

    rep(i, 4) {
        rep(j, 4) {
            cout << c[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
