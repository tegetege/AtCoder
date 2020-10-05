#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    string s;
    int cnt=0;
    rep(i, 12){
        cin >> s;
        if (s.find("r") != string::npos ){
            ++cnt;
        }
    }

    cout << cnt <<"\n";
    return 0;
}
