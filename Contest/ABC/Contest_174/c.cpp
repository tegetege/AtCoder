#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    string tar, K;
    cin >> K;

    int k = atoi(K.c_str());
    if (k % 2 == 0) {
        cout << -1 << endl; 
        return 0;
    }

    int cnt = K.length();
    while(true) {
        string target = string(cnt, '7');
        if (atoi(target.c_str()) % k == 0) {
            cout << cnt << "\n";
            return 0;
        }
        ++cnt;
    }



    return 0;
}
