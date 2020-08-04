#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N;
    string status;
    map<string, int> mp;
    mp["AC"] = 0;
    mp["WA"] = 0;
    mp["TLE"] = 0;
    mp["RE"] = 0;

    cin >> N;
    rep(i, N) {
        cin >> status;
        mp[status] += 1;
    }

    cout << "AC x " << mp["AC"] << endl;
    cout << "WA x " << mp["WA"] << endl;
    cout << "TLE x " << mp["TLE"] << endl;
    cout << "RE x " << mp["RE"] << endl;

    return 0;
}
