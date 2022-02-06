#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int H, W;
    cin >> H >> W;
    vector<vector <char>> a(H, vector<char>(W));
    rep(i, H) {
        rep(j, W) {
            cin >> a[i][j];
        }
    }

    // 入力確認
    // for (auto e: a) {
    //     for (auto i: e) {
    //         cout << i ;
    //     } cout << endl;
    // }

    vector<vector <ll>> DP(H+1, vector<ll>(W+1, 0));
    cout << "DP確認" << endl;
    for (auto e: DP) {
        for (auto i: e) {
            cout << i ;
        } cout << endl;
    }

    DP[0][0] = 1; // スタート
    for(int i=0; i < H; ++i) {
        for(int j=0; j < W; ++j) {
            cout << "i : j = " << i << j << endl;
            // 右 (もらうDP)
            if (a[i][j+1] == '.') {
                cout << "DP[i][j+1]" << DP[i][j+1] << endl;
                cout << "DP[i][j]" << DP[i][j] << endl;
                DP[i][j+1] = (DP[i][j+1] + DP[i][j]) % 1000000007; // ここでsegmentation faultが発生
            }
            // 下
            if (a[i+1][j] == '.') {
                DP[i+1][j] = (DP[i+1][j] + DP[i][j]) % 1000000007;
            }
        }
    }

    cout << DP[H][W] << endl;


    // 入力確認
    cout << "出力確認" << endl;
    for (auto e: DP) {
        for (auto i: e) {
            cout << i ;
        } cout << endl;
    }
    return 0;
}
