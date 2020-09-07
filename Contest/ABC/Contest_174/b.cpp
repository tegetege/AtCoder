#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N, cnt = 0, x, y;
    long long D, x, y;
    cin >> N >> D;
    D = D * D;
    
    rep(i, N) {
        cin >> x >> y;
        if ((x*x + y*y) <= D){
            ++cnt;
        }
    }
    cout << cnt << endl;

    return 0;
}
