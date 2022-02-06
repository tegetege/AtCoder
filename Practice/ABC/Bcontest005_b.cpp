#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int N, res = 101, target;
    cin >> N;

    rep(i, N){
        cin >> target;
        res = min(res,target);
    }

    cout << res << endl;


    return 0;
}
