#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    long long X, K, D;
    cin >> X >> K >> D;

    if (abs(X) / D != 0) {
        if ((abs(X) / D) <= K) {
            K = K - (abs(X) / D); // 一番絶対値に近いところにまず行く
            X = abs(X) - D * (abs(X) / D);
        } else {
            X = abs(abs(X) - D * K);
            K = 0;
        }
    }
    // cout << X << ":" << K << ":" << D << endl;

    
    
    if (K % 2 == 0){
        cout << abs(X) << endl;
        return 0;
    } else {
        cout << abs(X - D) << endl;
        return 0;
    }
    
    // ボツになった方法
    // if (D == abs(X)) {
    //     if (K % 2 == 0){
    //         // Kが偶数
    //         cout << abs(X) << endl;
    //         return 0;
    //     } else {
    //         // Kが奇数
    //         cout << 0 << endl;
    //         return 0;
    //     } 
    // } else if (D < abs(X)) {
    //     if (K % 2 == 0){
    //         // Kが偶数
    //         cout << abs(abs(X) - D*2) << endl;
    //         return 0;
    //     } else {
    //         // Kが奇数
    //         cout << abs(abs(X) - D) << endl;
    //         return 0;
    //     } 
    // } else if (D > abs(X) and D < abs(X)*2) {
    //     if (K % 2 == 0){
    //         // Kが偶数
    //         cout << abs(X) << endl;
    //         return 0;
    //     } else {
    //         // Kが奇数
    //         cout << abs(abs(X) - abs(D)) << endl;
    //         return 0;
    //     }
    // } else if (D == abs(X)*2){
    //     cout << abs(X) << endl;
    //     return 0;
    // }else {
    //     // D が　abs(X)の２倍以上の時
    //     if (K % 2 == 0){
    //         // Kが偶数
    //         cout << abs(X) << endl;
    //         return 0;
    //     } else {
    //         // Kが奇数
    //         cout << D << endl;
    //         return 0;
    //     }
    // }
    

    

    return 0;
}
