#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int N, left = 0, right = 0;
    
    cin >> N;
    vector<int> a(N);
    rep(i, N) {
        cin >> a.at(i);
    }

    ll count_ans = 0;

    for (int left = 0; left < N; ++left) {
        if (right != 0) {
            while (right < N && a[right - 1] < a[right]) {
                ++right;
            }
        }
       
        // cout << left << ":" << right << "=" << (right - left) << "\n";
        if (left != right) {
            count_ans += (right - left)+1;
        }

        if(right == left) {
            ++count_ans;
            ++right;
        }
    }
    cout << count_ans << "\n";
    
    return 0;
}
