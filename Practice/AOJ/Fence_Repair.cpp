/*
http://poj.org/problem?id=3253

[8,5,8](=21)の場合、
21 + (21-8=13) = 34
つまり、一回のカットする長さは長い方が良いので、ソートして長い順にカットするようにアルゴリズムを作成する
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    ll N, L_i, long_boad=0, cost=0;
    cin >> N;
    vector<ll> L(N);
    rep(i, N) {
        cin >> L[i];
        long_boad = long_boad + L[i];
    }
    sort(L.begin(), L.end()); // 昇順ソート

    // for(auto e : L) {
    //     cout << e << " ";
    // } cout << endl;
    
    cost = long_boad;

    // 長い部分からカットしていく
    for (int i = N; i > 2; i-- ) {
        cost = cost + (long_boad - L[i-1]);
        long_boad = long_boad - L[i-1];
        L.pop_back();
    }
    cout << cost << endl;
    return 0;
}
