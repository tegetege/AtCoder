#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int N, M,a, b;
    cin >> N >> M;
    vector<int> ans(N+1, 0);
    rep(i, M) {
        cin >> a >> b;
        ans[a]++; ans[b]++;
    }
    ans.erase(ans.begin());
    for (int i: ans) {
        cout << i << "\n";
    }

    return 0;
}
