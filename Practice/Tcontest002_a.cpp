// AtCoder Typical Contest002
// https://atcoder.jp/contests/atc002/tasks/abc007_3
// 参考
// https://atcoder.jp/contests/atc002/submissions/13536993

#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < (n); i++)
#define rep_row(i,n) for (int i = 0; i < (n-1); i++)

vector<string> c;

int main() {
    int R, C, s_y, s_x, g_y, g_x;

    // インプット
    cin >> R >> C;
    cin >> s_y >> s_x;
    cin >> g_y >> g_x;
    c.resize(R);
    s_y--;
    s_x--;
    g_y--;
    g_x--;
    rep(i,R) {
        cin >> c[i]; // マス情報をインプット
    }

    // 2次配列 (x, y)までのステップ数を格納
    vector<vector<int>> dist(R, vector<int>(C, -1)); 
    // キュー
    queue<pair<int, int>> que;

    // 初期値入力
    dist[s_y][s_x] = 0;
    que.push(make_pair(s_y, s_x)); // (x, y)座標

    // 考えているセルからの移動
    int d_y[] = {1, 0, -1, 0};
    int d_x[] = {0, 1, 0, -1};

    // キューが空になったら終了
    while(!que.empty()) {
        pair<int, int> now = que.front();  que.pop(); // 今から考えるセル
        
        for (int i = 0; i < 4; i++) {
            // 考えているセルからの移動 ↓→↑←
            int n_y = now.first + d_y[i];
            int n_x = now.second + d_x[i];

            if (0 <= n_y && n_y <= R && 0 <= n_x && n_x <= C && 
                    c[n_y][n_x] != '#' && dist[n_y][n_x] == -1) {
                // now のセルの隣のセルが行けたらキューに追加する
                que.push(make_pair(n_y, n_x));
                dist[n_y][n_x] = dist[now.first][now.second] + 1;
            }
        }
    }

    cout << dist[g_y][g_x] << endl;
}
