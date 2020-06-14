#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int X, N, target = 1000, ans = 1000;
    cin >> X >> N;
    if (N != 0) { 
        // vector<int> P(N);
        vector<int> able(102-N);

        for(int i = -1; i <= 101; i++) {
            able[i+1] = i;
        }
        cout << endl;
        sort(able.begin(), able.end());
        rep(i, 103) { 
            cout << able[i] << " ";
        }
        cout << endl;
        

        rep(i, N) {
            cin >> target;
            target ++;
            remove(able.begin(), able.end(), target); // 入力値を消す
        }

        rep(i, able.size()){
            cout << able[i] << " ";
        }
        cout << endl;
        
        rep(i, able.size()){
            if (target >= abs(N - able.at(i))) {
                if (target == abs(N - able.at(i))) {
                    ans = min(ans, i-1);
                } else {
                    target = abs(N - able.at(i));
                    ans = i-1;
                }
            }
        }
        cout << ans << endl;

    } else {
        cout << N << endl;
        return 0;
    }

    




    return 0;
}
