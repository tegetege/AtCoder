#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    // 入力
    int N, inp_1, inp_2, L, P;
    cin >> N;

    int A[N + 1], B[N + 1];
    rep(i, N) {
        cin >> A[i] >> B[i];
    }
    cin >> L >> P;

    priority_queue<int> que;

    int ans = 0, pos = 0, tank = P;

    for (int i = 0; i < N; ++i) {
        int d = A[i] - pos; // 進む距離
        // もし、次に進む距離分のガソリンがない場合、その前で給油したことにしてから移動する
        while (tank - d < 0) {
            if (que.empty()) {
                puts("-1");
                return 0;
            }
            tank += que.top(); que.pop();
            ++ans;
        }

        tank -= d;
        pos = A[i];
        que.push(B[i]);
    }

    cout << ans << endl;

    return 0;
}
