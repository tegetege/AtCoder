#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    long long X;
    cin >> X;
    for (long long i = 0; i*i*i*i <= X; ++i) {
        if (i*i*i*i == X) {
            cout << i << endl;
            return 0;
        }
    }
    return 0;
}
