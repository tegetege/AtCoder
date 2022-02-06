#include <bits/stdc++.h>
using namespace std;

int main() {
    int A, B, C, D, T, aoki;
    cin >> A >> B >> C >> D;

    T = A / D;
    if (A % D != 0) T++;
    aoki = C / B;
    if (C % B != 0) aoki++;
    if (T >= aoki) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

}
