#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    string s, t;
    cin >> s;
    cin >> t;
    
    
    vector<vector<int>> DP(s_size+1, vector<int>(t_size+1, 0));

    // for (int i = 1; i <= s_size; ++i) {
    //     for (int j = 1; j <= t_size; ++j) {
    //         if (s[i-1] == t[j-1]) {
    //             // cout << i << " : " << j << " => " << s[i-1] << endl;
    //             DP[i][j] = DP[i-1][j-1]+1; 
    //         } else {
    //             DP[i][j] = max(DP[i-1][j], DP[i][j-1]);
    //         }
    //     }
    // }

    for (int i = s_size; 1 < i; --i) {
        for (int j = t_size; 1 < j; --j) {
            if (s[i-1] == t[j-1]) {
                // cout << i << " : " << j << " => " << s[i-1] << endl;
                DP[i][j] = DP[i-1][j-1]+1; 
            } else {
                DP[i][j] = max(DP[i-1][j], DP[i][j-1]);
            }
        }
    }

    string ans = "";
    while(s_size!=0 && t_size!=0) {
        if(DP[s_size-1][t_size]==DP[s_size][t_size]) {
            --s_size;
        } else if(DP[s_size][t_size-1]==DP[s_size][t_size]) {
            --t_size;
        } else {
            ans = t[t_size-1]+ans;
            --s_size; --t_size;
        }
    }
    cout << ans << endl;
    return 0;
}
