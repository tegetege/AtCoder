#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string s;
    cin >> s;
    cout << s.at(0) + to_string(s.size() - 2) + s.at(s.size()-1) << endl;
    return 0;
}
