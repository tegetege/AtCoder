// https://cses.fi/problemset/task/1068/
// コラッツ予想(Collatz conjecture)

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    ll n;
    cin >> n;
    cout << n << " ";
    while(n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = n * 3 +1;
        }
        cout << n << " ";
    }
    cout << "\n";
    return 0;
}
