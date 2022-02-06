#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int L, H, N, target;
    
    cin >> L >> H;
    cin >> N;
    vector<int> ans;

    rep(i, N) {
        cin >> target;
        ans.push_back(target);
    }

    rep(i, N) {
        if (ans[i] > H) {
            cout << -1 << "\n";
        } else if(ans[i] < L) {
            cout << L - ans[i] << "\n";
        } else {
            cout << 0 << "\n";
        }
    }

    return 0;
}
