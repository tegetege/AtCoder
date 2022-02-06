#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    string w;
    map<char, int> mp;
    cin >> w;

    rep(i, w.length()) {
        if (mp[w[i]] == 0) {
            mp[w[i]] = 1;
        } else {
            mp[w[i]] += 1;
        }
    }

    for (const auto& [key, value] : mp) {
        if (value % 2 != 0) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl; 

    return 0;
}
