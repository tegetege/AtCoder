#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int R, C, s_y, s_x, g_y, g_x;
    cin >> R >> C;
    cin >> s_y >> s_x;
    --s_y; --s_x;
    cin >> g_y >> g_x;
    --g_y;--g_x;
    vector<vector <char>> c(R, vector<char>(C));
    vector<vector <int>> ans(R, vector<int>(C));
    queue<pair<int, int>> que;
    rep(i, R) {
        rep(j, C) {
            cin >> c[i][j];
        }
    }

    int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};

    que.push(make_pair(s_y, s_x));
    c[s_y][s_x] = '#';
    ans[s_y][s_x] = 0;
    while (!que.empty()){
        pair<int, int> now = que.front(); que.pop();
        if (now.first == g_y && now.second == g_x) {
            break;
        }
        for(int i = 0; i < 4; ++i) {
            int ny = now.first + dy[i], nx = now.second + dx[i];
            if (0 <= ny && ny < R && 0 <= nx && nx < C && c[ny][nx] != '#') {
                que.push(make_pair(ny, nx));
                ans[ny][nx] = ans[now.first][now.second] + 1;
                c[ny][nx] = '#';
            }
        }
    }

    // 結果の表示
    // for(auto e : ans) {
    //     for(auto f : e) {
    //         cout << f << " ";
    //     }cout << endl;
    // }cout << endl;

    cout << ans[g_y][g_x] << endl;
    return 0;
}
