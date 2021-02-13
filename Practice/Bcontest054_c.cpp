#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"


using Graph = vector<vector<int> >;
Graph G;

void dfs(int v, vector<bool> &seen, int &res) {
    bool end = true;
    for(int i = 0; i < seen.size(); ++i) {
        if (!seen[i] && i != v) {
            end = false;
        }
    }
    if (end) {
        ++res;
        return;
    }

    seen[v] = true;
    for (auto nv : G[v]) {
        if (seen[nv]) continue;
        dfs(nv, seen, res);
    }
    seen[v] = false;
}

int main() { 
    int N, M, a, b;
    cin >> N >> M;
    G.assign(N, vector<int>()); // 縦N行の2次元配列
    rep(i, M) {
        cin >> a >> b; --a, --b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    vector<bool> seen(N, false);
    int res = 0;
    dfs(0, seen, res);
    cout << res << endl;

    return 0;
}
