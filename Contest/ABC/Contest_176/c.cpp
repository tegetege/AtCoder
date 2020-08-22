#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int N;
    long long ans=0;
    cin >> N;
    vector<long long> A(N);
    rep(i, N) {
        cin >> A.at(i);
    }

    for(int i = 1; i < N; ++i) {
        if (A[i-1] > A[i]) {
            // 前の人が高い場合
            ans += A[i-1] - A[i];
            A[i] += A[i-1] - A[i];
        }
    }
    cout << ans << endl;



    return 0;
}
