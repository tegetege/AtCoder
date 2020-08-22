#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int H, W, C_h, C_w, D_h, D_w;
    cin >> H >> W;
    cin >> C_h >> C_w;
    cin >> D_h >> D_w;
    vector<vector<char>> S(H+10, vector<char>(W+10));
    vector<vector<int>> DP(H+10, vector<int>(W+10, 10000));

    rep(i, H) {
        rep(j, W) {
            cin >> S.at(i+5).at(j+5);
        }
    }
    

    rep(i, H) {
        rep(j, W) {
            cout << S[i][j] << " ";
        }
        cout << endl;
    }

    
    if (C_h <= D_h) {
        // C_hの方が上の場合
        if (C_w >= D_w) {
            // Cに対してDが左上にある場合
            for (int i = C_h+5; i >= 6; --i) {
                for(int j = C_w+5; j >= 6; --j) {
                    if (i == C_h+5 and j == C_w+5) {
                        DP[C_h+5][C_w+5] = 0; // スタート地点
                    }

                    // 歩いて行ける距離
                    if(S[i-1][j] == '.') {
                        DP[i-1][j] = min(DP[i][j], DP[i-1][j]); //上
                    }
                    if (S[i][j+1] == '.') {
                        DP[i][j+1] = min(DP[i][j], DP[i][j+1]); //みぎ
                    }
                    if (S[i+1][j] == '.') {
                        DP[i+1][j] = min(DP[i][j], DP[i+1][j]); //下
                    }
                    if (S[i][j-1] == '.') {
                        DP[i][j-1] = min(DP[i][j], DP[i][j-1]); //ひだり
                    }

                    // ワープを利用する
                    for (int k = i-2 ; k <= i+2; ++k) {
                        for (int l = j-2; j <= j+2; ++j) {
                            if (S[k][l] == '.') {
                                DP[k][l] = min(DP[i][j]+1, DP[k][l]);
                            }
                        }
                    }
                }
            }
        } else {
            // Cに対してDが右上にある場合 
            for (int i = C_h+5; i >= 6; --i) {
                for(int j = C_w+5; j <= W+5; ++j) {
                    if (i == C_h+5 and j == C_w+5) {
                        DP[C_h+5][C_w+5] = 0; // スタート地点
                    }
                    // 歩いて行ける距離
                    if(S[i-1][j] == '.') {
                        DP[i-1][j] = min(DP[i][j], DP[i-1][j]); //上
                    }
                    if (S[i][j+1] == '.') {
                        DP[i][j+1] = min(DP[i][j], DP[i][j+1]); //みぎ
                    }
                    if (S[i+1][j] == '.') {
                        DP[i+1][j] = min(DP[i][j], DP[i+1][j]); //下
                    }
                    if (S[i][j-1] == '.') {
                        DP[i][j-1] = min(DP[i][j], DP[i][j-1]); //ひだり
                    }
                    cout << "移動完了" << endl;
                    // ワープを利用する
                    for (int k = i-2 ; k <= i+2; ++k) {
                        for (int l = j-2; j <= j+2; ++j) {
                            if (S[k][l] == '.') {
                                DP[k][l] = min(DP[i][j]+1, DP[k][l]);
                            }
                        }
                    }
                    cout << i << ":" << j << " 完了" <<endl;
                }
            }
        }
    } else {
        // C_hの方が下の場合
        if (C_w >= D_w) {
            // Cに対してDが左下にある場合
            for (int i = C_h+5; i <= H+5; ++i) {
                for(int j = C_w+5; j >= 6; --j) {
                    if (i == C_h+5 and j == C_w+5) {
                        DP[C_h+5][C_w+5] = 0; // スタート地点
                    }

                    // 歩いて行ける距離
                    if(S[i-1][j] == '.') {
                        DP[i-1][j] = min(DP[i][j], DP[i-1][j]); //上
                    }
                    if (S[i][j+1] == '.') {
                        DP[i][j+1] = min(DP[i][j], DP[i][j+1]); //みぎ
                    }
                    if (S[i+1][j] == '.') {
                        DP[i+1][j] = min(DP[i][j], DP[i+1][j]); //下
                    }
                    if (S[i][j-1] == '.') {
                        DP[i][j-1] = min(DP[i][j], DP[i][j-1]); //ひだり
                    }

                    // ワープを利用する
                    for (int k = i-2 ; k <= i+2; ++k) {
                        for (int l = j-2; j <= j+2; ++j) {
                            if (S[k][l] == '.') {
                                DP[k][l] = min(DP[i][j]+1, DP[k][l]);
                            }
                        }
                    }
                }
            }
        } else {
            // Cに対してDが右下にある場合 
            for (int i = C_h+5; i <= H+5; ++i) {
                for(int j = C_w+5; j <= W+5; ++j) {
                    if (i == C_h+5 and j == C_w+5) {
                        DP[C_h+5][C_w+5] = 0; // スタート地点
                    }

                    // 歩いて行ける距離
                    if(S[i-1][j] == '.') {
                        DP[i-1][j] = min(DP[i][j], DP[i-1][j]); //上
                    }
                    if (S[i][j+1] == '.') {
                        DP[i][j+1] = min(DP[i][j], DP[i][j+1]); //みぎ
                    }
                    if (S[i+1][j] == '.') {
                        DP[i+1][j] = min(DP[i][j], DP[i+1][j]); //下
                    }
                    if (S[i][j-1] == '.') {
                        DP[i][j-1] = min(DP[i][j], DP[i][j-1]); //ひだり
                    }

                    // ワープを利用する
                    for (int k = i-2 ; k <= i+2; ++k) {
                        for (int l = j-2; j <= j+2; ++j) {
                            if (S[k][l] == '.') {
                                DP[k][l] = min(DP[i][j]+1, DP[k][l]);
                            }
                        }
                    }
                }  
            }
        }
    }
    cout << DP[C_h+5][C_w+5] << endl;



    return 0;
}
