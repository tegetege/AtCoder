/*
http://poj.org/problem?id=2431

牛のグループはガソリンがリークしたトラックで走る必要がある。
ゴールの街までN箇所の給油所があり、そこではガソリンを補充することができる
街までLの距離が離れてて、現在のガソリンの量はP残っている状態
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int N, inp_1, inp_2, L, P;
    cin >> N;
    vector<pair<int, int>> gas;
    rep(i, N) {
        cin >> inp_1 >> inp_2;
        gas.push_back(make_pair(inp_1, inp_2));
    }
    cin >> L >> P;
    
    // 2次元配列gasのinp_1を基準に昇順ソートしたいけど、方法がわからない
    // sort(gas.begin(), gas.end(),)

    int stop=0; // ストップ回数
    for(int i = N; i >= 1; i--) {
        if ( L - gas[i - 2].first >= P) {
            ++stop;
            P = P - (L - gas[i - 1].first) + gas[i - 1].second; // P - 走った距離 + 入れたガソリン
            L = gas[i - 1].first;
            // cout << "stop! 残り距離: " << L << ", ガス残り: " << P << endl;
        }

        if (P >= L) {
            break;
        }
    }
    cout << stop << endl;

    return 0;
}
