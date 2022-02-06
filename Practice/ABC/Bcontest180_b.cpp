#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    ll N, man=0, yu=0, che=0, inp;
    cin >> N;
    rep(i, N) {
        cin >> inp;
        man += abs(inp);
        yu += abs(inp) * abs(inp);
        che = max(che, abs(inp));
    }
    double yu_d = yu * 1.0;
    double yu_ans = pow(yu_d, 0.5);

    cout << man << endl;
    // cout << yu_ans << endl;
    printf("%.13f \n", yu_ans);
    cout << che << endl;
    
    return 0;
}
