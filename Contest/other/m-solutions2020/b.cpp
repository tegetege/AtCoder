#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

bool judgment(int A, int B, int C) {
    if (A < B && B < C) {
        // cout << A << " " << B << " " << C << " " << endl;
        cout << "Yes" << endl;
        return true;
    } else {
        // cout << A << " " << B << " " << C << " " << endl;
        return false;
    }
}


int main() {
    int A, B, C, K, cnt = 0;
    cin >> A >> B >> C;
    cin >> K;

    rep (i, K) {
        if (B <= A) {
            B *= 2;
            ++cnt;
        } else if (C <= B) {
            C *= 2;
            ++cnt;
        } 

        if (judgment(A,B,C)) {
            return 0;
        } else {
            continue;
        }
        
    }
    
    if (A < B && B < C) {
        cout << "Yes" << endl;
        return 0;
    } else {
        cout << "No" << endl;
        return 0;
    }

    return 0;
}
