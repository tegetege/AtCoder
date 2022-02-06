#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    int N, T, A, pre_time=-1;
    ll ans=0;
    cin >> N >> T;

    rep(i, N) {
        cin >> A;
        if (pre_time == -1) {
            pre_time = A;
        } else { 
            if (abs(pre_time - A) <= T) {
                ans += abs(pre_time - A);
                pre_time = A;
            } else if (abs(pre_time - A) > T){
                ans += T;
                pre_time = A;
            }
        }
    }
    ans += T;
    cout << ans << endl;
    return 0;
}
