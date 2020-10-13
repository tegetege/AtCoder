#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int main() { 
    int  H, W, K, cnt=0, ans=0;
    string c_in, target_row;
    cin >> H >> W >> K;
    vector<string> c(H);
    rep(i, H){
        cin >> c.at(i);
    }

    for(int i = 0; i < H; ++i) {
        // 行を何行とる？
        for(int i_ = 0; i_ < H; ++i_) {
            // 行を何行からとる？その行に含まれている黒いマスは何個？
            cnt += count(c[i+i_].cbegin(), c[i+i_].cend(), '#');
            c[i+i_] = regex_replace(c[i+i_], regex("#"), "#_"); //数えた#は#_へ置換
        }

        for(int j = 0; j < W; ++j) {
            // 列を何列とる?
            for(int j_ = 0; j_ < W; ++j_) {
                // 列を何列からとる？
                // 赤く塗る部分は何マスある？
            }   
        }
        if (cnt == K)
    }

    cout << "hoge" <<"\n";
    return 0;
}


