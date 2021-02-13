#include <bits/stdc++.h> 
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
int n, m;
vector<vector<char>> grid(m, vector<char>(n));
void dfs(int i, int j) {
    grid[i][j] = '.';
    for(int dx = -1; i <= 1; i ++) {
        for(int dy = -1; j <= 1; j++) {
            int nx = i + dx;
            int ny = j + dy;
            if ( 0 <= nx && nx <= n-1 && 0 <= ny && ny <= m-1) {
                dfs(nx, ny);
            }
        }
    }
    return;
}
int main() {
    cin >> n >> m;
    int input;
    rep(i, n) {
        grid.push_back(vector<char>());
        rep(j, m) {
            cin >> input;
            grid[i].push_back(input);
        }
    }

    cout << "入力完了" << endl;
    int res = 0;
    rep(i, n) {
        rep(j, m) {
            if (grid[i][j] == 'W') {
                dfs(i,j);
                res++;
            }
        }
    }
    cout << res << endl;
    return 0;
}
