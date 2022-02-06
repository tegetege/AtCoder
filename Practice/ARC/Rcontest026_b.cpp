#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int main() {
    long long N, cnt = 0;
    cin >> N;

    // Nに1が入力されることを考慮する
    for(long long i = 1; i * i <= N; ++i) {
        if (N % i == 0) {
            cnt += i;
            cnt += N/i;
            if (i * i == N) {
                cnt -= i;
            }
        }
    }
    cnt -= N; // i = 1の時、Nが入ってしまうので、それを除く


    if (cnt == N) {
        cout << "Perfect" << endl;
    } else if (cnt < N) {
        cout << "Deficient" << endl;
    } else if (cnt > N) {
        cout << "Abundant" << endl;
    }

    return 0;
}
