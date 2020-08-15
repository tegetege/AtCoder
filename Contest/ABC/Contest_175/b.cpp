#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)


int main() { 
    int N, count = 0;
    cin >> N;
    vector<long long> L(N);
    rep(i, N){
        cin >> L.at(i);
    }

    for(int i = 0; i < N - 2; ++i) {
        for (int j = i+1; j < N - 1; ++j) {
            for (int k = j+1; k < N; ++k) {
                // cout << i << j << k << " : ";
                vector<long long> p = {L[i], L[j], L[k]};
                sort(p.begin(), p.end());
                // cout << p[0] << p[1] << p[2] << endl;
                auto result = unique(p.begin(), p.end());
                p.erase(result, p.end());
                // cout << p[0] << endl;
                if (p.size() == 3) {
                    if (p[2] < p[0] + p[1]) {
                        // cout << i+1 << j+1 << k+1 << " : "<< p[0] << p[1] << p[2] << endl;
                        ++count;
                    }
                }
            }
        }
    }
    cout << count << endl;

    return 0;
}
