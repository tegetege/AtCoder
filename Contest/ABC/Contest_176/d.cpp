#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int H, W, C_h, C_w, D_h, D_w;
    cin >> H >> W;
    cin >> C_h >> C_w; // スタート
    cin >> D_h >> D_w; // ゴール
    --C_h; --C_w;
    --D_h; --D_w;
    vector<string> S(H);

    // 迷路をインプット
    rep(i, H) {
        rep(j, W) {
            cin >> S.at(i);
        }
    }
    
    // 2次元配列 (D_h, D_w)までのステップ数を格納
    vector<vector <int>> dist(H, vector<int>(W, -1));
    // キュー
    queue<pair<int, int>> que;
    //初期値入力
    dist[C_h][C_w] = 0;
    que.push(make_pair(C_h, C_w));
    // 考えているセルからの移動
    int d_y[] = {1, 0, -1, 0};
    int d_x[] = {0, 1, 0, -1};
    // ワープ魔法で移動する
    int warp_y[] = {};
    int warp_x[] = {};
    int count = 0;
    for (int y = 0; y < 5; ++y) {
        for (int x = 0; x < 5; ++x) {
            warp_y[count] = -2 + y;
            warp_x[count] = -2 + x;
            ++count;
        }
    }

    while(!que.empty()) {
        pair<int, int> now = que.front(); que.pop();
        int count = 0;

        for (int i = 0; i < 4; i++) {
            int n_y = now.first + d_y[i];
            int n_x = now.second + d_x[i];

            if (0 <= n_y && n_y <= H && 0 <= n_x && n_x <= W &&
                    S[n_y][n_x] != '#') {
                        que.push(make_pair(n_y, n_x));
                        if (dist[n_y][n_x] == -1) {
                            dist[n_y][n_x] = dist[now.first][now.second];
                            ++count;
                        } else {
                            dist[n_y][n_x] = min(dist[n_y][n_x], dist[now.first][now.second]);
                        }
                        
                    }
        }

        // 魔法を使って移動できる場所を探す
        if (count == 0) {
            for (int i = 0; i < 25; ++i) {
                int n_y = now.first + warp_y[i];
                int n_x = now.second + warp_x[i];

                if (0 <= n_y && n_y <= H && 0 <= n_x && n_x <= W &&
                    S[n_y][n_x] != '#') {
                        if (dist[n_y][n_x] == -1) {
                            que.push(make_pair(n_y, n_x));
                            dist[n_y][n_x] = dist[now.first][now.second] + 1;
                        } else {
                            // dist[n_y][n_x] = min(dist[n_y][n_x], dist[now.first][now.second] + 1);
                            if (dist[n_y][n_x] > dist[now.first][now.second] + 1) {
                                dist[n_y][n_x] = dist[now.first][now.second] + 1;
                                que.push(make_pair(n_y, n_x));
                            }
                        }

                    }

            }
        }

    }

    cout << dist[D_h][D_w] << endl;
    
    return 0;
}
