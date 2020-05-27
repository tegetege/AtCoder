#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); i++)
using namespace std;

const int INF = 2000008;

// 隣接リスト グラフ, 可変長配列
vector<int> to[100005];

int main() {
    int n, m;
    cin >> n >> m;
    rep(i,m) {
        int a, b;
        cin >> a >> b;
        --a; --b; // 扱いやすいように0スタートにする(decrement)
        
        // 各頂点ごとに配列を持っておき、繋がっている頂点のリストをもつ
        to[a].push_back(b);
        to[b].push_back(a);
    }

    queue<int> q;
    vector<int> dist(n, INF);
    vector<int> pre(n, -1);
    dist[0] = 0;
    q.push(0);
    // 計算量　o(2N) (o(N))
    //  ⇨ 各頂点一回ずつしかみていない
    while(!q.empty()) {
        int v = q.front(); q.pop(); 
        for (int u : to[v]) { // to[v] = 頂点vの隣の頂点のリスト
            if (dist[u] != INF) continue; // その頂点の距離がわかっている時　
            dist[u] = dist[v] + 1;
            pre[u] = v; // 頂点uに繋がる、(一個手前の)頂点v
            q.push(u);
        }
    }

    // 結果の出力
    cout << "Yes" << endl; // この問題は常に"Yes" らしい(?)
    rep(i,n) {
        if (i == 0) continue;
        int ans = pre[i];
        ++ans;
        cout << ans << endl;
    }

    return 0;
}
