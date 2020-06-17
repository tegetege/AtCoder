#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

vector<int> to[100005];
int dp[100005], dag[100005];

int main() {
    long N, M;
    cin >> N >> M;

    rep(i, 100005) {
        dp[i] = 0; // 距離
        dag[i] = 0; // 入次数
    }

    rep(i, M) {
        int x, y;
        cin >> x >> y;
        x--, y--;
        to[x].push_back(y);
        dag[y]++;
    }

    queue<int> que;
    rep(i,N) {
        if (dag[i] == 0) {
            que.push(i);
        }
    }

    while(!que.empty()) {
        int v = que.front(); que.pop();

        for (int nv : to[v]) {
            dag[nv]--;
            if (dag[nv] == 0) {
                que.push(nv);
                dp[nv] = max(dp[nv], dp[v] + 1);
            }
        }
    }

    int res = 0;
    rep(i, N) {
        res = max(res, dp[i]);
    }
    cout << res << endl;

    return 0;
}
