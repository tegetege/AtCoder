// 問題:https://atcoder.jp/contests/dp/tasks/dp_i
// 参考:https://misora192.hatenablog.com/entry/2019/01/07/081144

#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < (n); i++)


int main(void) {
    int N;
    cin >> N;
    double p[N];
    rep(i, N) cin >> p[i];



    double dp[N+1][N+1];
    rep(i,N+1){
        rep(j,N+1){
            dp[i][j] = 0.0;
        }
    }

    dp[0][0] = 1.0;
    for(int i = 1; i <= N; i++) {
        for(int j = 0; j <= i; j++) {
            if(j >= 1){
                dp[i][j] = dp[i-1][j-1] * p[i-1] + dp[i-1][j] * (1.0 - p[i-1]);
            } else {
                dp[i][j] = dp[i-1][j] * (1.0 - p[i-1]);
            }
        }
    }

    // rep(i,N+1){
    //     rep(j,N+1){
    //         cout << dp[i][j] << endl;
    //     }
    // }

    double ans = 0.0;
    for(int i = (N/2)+1; i <= N; i++) {
        // cout << dp[N][i] << endl;
        ans += dp[N][i];
    }
    // 浮動小数点数を出力する精度を設定する(制約10桁)
    cout << setprecision(10) << scientific << ans << endl;

    return 0;
}
