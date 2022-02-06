#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    string X_str;


    cin >> N;
    cin >> X_str;
    vector<int> X(N);
    rep(i, N) {
        X[i] = (int)(X_str[i] - 48);
    }

    rep(i, N) {
        cout << X[i] << " ";   
    }
    cout << endl;


    return 0;
}
