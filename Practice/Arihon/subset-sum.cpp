// P34:部分和問題

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

bool dfs(int i, ll sum, int n, ll k, vector<ll> a) {
    if (i == n) {
        return k == sum;
    }
    if (dfs(i+1, sum, n, k, a)) {
        return true;    // a[i]を使う場合
    }
    if (dfs(i+1, sum+a[i], n, k, a)) {
        return true;    // // a[i]を使わない場合
    }
    return false;
}

int main() { 
    int n;
    
    ll k;
    cin >> n;
    vector<int> a(n);
    rep(i, n) {
        cin >> a.at(i);
    }
    
    cin >> k;

    if (dfs(0, 0, n, k, a)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}

// (base) [Arihon]  (master *)$./a.out 
// 4
// 1 2 4 7 
// 13
// Yes
