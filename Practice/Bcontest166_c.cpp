#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int N, M;
    cin >> N >> M;
    vector<int> H(N);
    vector<bool> ok(N, true);
    rep(i, N) {
        cin >> H.at(i);
    }

    rep(i, M) {
        // グラフ構造は持たず、それぞれのインプットで考えていく
        int A, B;
        cin >> A >> B;
        --A; --B;
        // 以下の条件を満たすとき、「良い展望台とは言えない」
        if (H[A] <= H[B]) ok[A] = false;
        if (H[B] <= H[A]) ok[B] = false;
    }
    int ans = 0;
    rep(i, N) {
        if (ok[i]) {
            ++ans;
        }
    }

    cout << ans << endl;
    return 0;
}
