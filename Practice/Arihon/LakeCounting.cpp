#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

vector<vector<char>> dfs(int x, int y, vector<vector<char>> garden, int N, int M) {
    garden[x][y] = '.'; // その場所を'.'に置き換える

    for(int i = -1; i <= 1; ++i) {
        for(int j = -1; j <= 1; ++j) {
            int next_N = x + i, next_M = y + j;
            if ((0 <= next_N && next_N < N) && (0 <= next_M && next_M < M) && garden[next_N][next_M] == 'W') {
                dfs(next_N, next_M, garden, N, M);
            }
        }
    }
    return garden;
}

int main() { 
    int N, M, res=0;
    cin >> N >> M;
    vector<vector <char>> garden(N, vector<char>(M, '*'));
    
    rep(i, N) {
        rep(j, M) {
            cin >> garden[i][j];
        }
    }

    rep(i, N) {
        rep(j, M) {
            vector<vector <char>> garden = dfs(i, j, garden, N, M);
            ++res;
            cout << i << " : " << j << endl;
        }
    }
    cout << res << endl;

    return 0;
}

// 実行するとメモリ関係で怒られちゃう
// (base) [Arihon]  (master *)$./a.out 
// 10 12
// W........WW.
// .WWW.....WWW
// ....WW...WW.
// .........WW.
// .........W..
// ..W......W..
// .W.W.....WW.
// W.W.W.....W.
// .W.W......W.
// ..W.......W.
// terminate called after throwing an instance of 'std::bad_alloc'
//   what():  std::bad_alloc
// Abort trap: 6
