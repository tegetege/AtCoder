#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

auto tonaments(vector<pair<int, int>> targets) {
    ll targets_length = targets.size();

    for(ll i = 0; i < targets_length / 2; ++i) {
        if (targets[i].second < targets[i+1].second) {
            targets.erase(targets.begin() + i);
        } else {
            targets.erase(targets.begin() + i + 1);
        }
    }
    
    if (targets.size() == 2) {
        return targets;
    } else {
        tonaments(targets);
    }
}


int main() { 
    int N;
    cin >> N;
    vector<pair<int, int>> A, finalist(2);
    rep(i, pow(2, N)) {
        ll a;
        cin >> a;
        A.push_back(make_pair(i+1, a));
    }

    finalist = tonaments(A); // ここでAbort trap: 6が発生
    cout << finalist[0].second << " : " << finalist[1].second << endl;
    if (finalist[0].second > finalist[1].second) {
        cout << finalist[1].first << endl;
    } else {
        cout << finalist[0].first << endl;
    }

    return 0;
}
