#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long target, i;
    cin >> target;

    for(int i = 2; i * i <= target; i++) {
        if (target % i == 0) {
            cout << "NO" << endl;
            return 0;
        } 
    }
    cout << "YES" << endl;

    return 0;
}
