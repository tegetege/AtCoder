// https://atcoder.jp/contests/m-solutions2020

#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int X;
    cin >> X;
    
    int target[] = {400, 600, 800, 1000, 1200, 1400, 1600, 1800};
    int count = 8;
    for (int i = 0; i < 7; ++i){
        if (X >= target[i] and X < target[i+1]) {
            cout << count << endl;
            return 0;
        } else if (X >= 1800 and X < 2000) { // ここのことを忘れてた
            cout << 1 << endl;
            return 0;
        }
        --count;
    }
    return 0;
}
