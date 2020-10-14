#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int main() { 
    int  H, W, K, cnt=0, ans=0;
    string c_in, target_row;
    cin >> H >> W >> K;
    vector<string> c(H);
    rep(i, H){
        cin >> c.at(i);
    }

    rep(is, 1 << H) {
        rep(js, 1 << W) {
            int cnt = 0;
            rep(i, H) rep(j, W) {
                // is >> i & 1
                // 2進数(is)のi桁目を取り出して(右シフト)、その１桁目を取り出す(& 1)
                if (is >> i&1) continue;
                if (js >> j&1) continue;
                if (c[i][j] == '#') cnt++;
            }
            if (cnt == K) ans++;
        }
    }

    cout << ans <<"\n";
    return 0;
}
