#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int n, x;
    string s;
    cin >> n >> x;
    cin >> s;
    for (int i=0; i < s.size(); ++i) {
        if (s[i] == 'o') {
            x += 1;
        } else {
            x = max(0, x-1);
        }
    }
    cout << x << endl;
    return 0;
}
