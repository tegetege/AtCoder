#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

vector<vector<ll>> dp_def(vector<vector<char>> a, vector<vector<ll>> DP, map<char, vector<pair<int, int>>> mp, pair<int, int> here, int H, int W) {
    int i = here.first, j = here.second;
    cout << i << " : " << j << endl;
    if (0 <= i and i <= H and 0 <= j and j <= W ) {
        if (a[i][j] != '#' or a[i][j] == 'G') {
            DP[i+1][j] = min(DP[i+1][j], DP[i][j]+1); // 右
            dp_def(a, DP, mp, make_pair(i+1, j), H, W);
            DP[i-1][j] = min(DP[i-1][j], DP[i][j]+1); // 左
            dp_def(a, DP, mp, make_pair(i-1, j), H, W);
            DP[i][j-1] = min(DP[i][j-1], DP[i][j]+1); // 上
            dp_def(a, DP, mp, make_pair(i, j-1), H, W);
            DP[i][j+1] = min(DP[i][j+1], DP[i][j]+1); // 下
            dp_def(a, DP, mp, make_pair(i, j+1), H, W);
            if (a[i][j] != '.') {
                // 英子文字の場合
                for (const auto& e: mp[a[i][j]]) {
                    DP[e.first][e.second] = min(DP[e.first][e.second], DP[i][j]+1);
                    dp_def(a, DP, mp, make_pair(e.first, e.second), H, W);
                }
            }
        } else {
            // "#"の場合
            return DP;
        }
        return DP;
    } else {
        return DP;
    }
}


int main() { 
    int H, W;
    cin >> H >> W;
    vector<vector<char>> a(H+1, vector<char>(W+1, '#'));
    vector<vector<ll>> DP(H+2, vector<ll>(W+2, 1000000007));
    map<char, vector<pair<int, int>>> mp; // {"a": [{1,3}, {4,8}...etc], "b":[...]}
    pair<int, int> S, G;
    for(int i=1; i <= H; ++i) {
        for (int j=1; j <= W; ++j) {
            cin >> a[i][j];
            if (a[i][j] == 'S') {
                S = make_pair(i, j);
                a[i][j] = '.';
            } else if (a[i][j] == 'G') {
                G = make_pair(i, j);
            }
            if (a[i][j] != '.') {
                // 英子文字の場合
                mp[a[i][j]].push_back(make_pair(i , j));
            }
        }
    }
    // for (const auto& e: mp['b']) {
    //     cout << e.first << " : " <<e.second << endl;
    // }

    DP[S.first][S.second] = 0;
    DP = dp_def(a, DP, mp, make_pair(S.first, S.second), H, W);
    // for (int i=1; i <= H; ++i) {
    //     for (int j=1; j <= W; ++j) {
    //         if (a[i][j] != '#') {
    //             DP[i+1][j] = min(DP[i+1][j], DP[i][j]+1); // 右
    //             DP[i-1][j] = min(DP[i-1][j], DP[i][j]+1); // 左
    //             DP[i][j-1] = min(DP[i][j-1], DP[i][j]+1); // 上
    //             DP[i][j+1] = min(DP[i][j+1], DP[i][j]+1); // 下
    //             if (a[i][j] != '.') {
    //                 // 英子文字の場合
    //                 for (const auto& e: mp[a[i][j]]) {
    //                     DP[e.first][e.second] = min(DP[e.first][e.second], DP[i][j]+1);
    //                 }
    //             }
    //         } else {
    //             // "#"の場合
    //             continue;
    //         }
    //     }
    // }
    if (DP[G.first][G.second] != 1000000007) {
        cout << DP[G.first][G.second] << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}
