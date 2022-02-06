#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

int main() { 
    ll N;
    char moji;
    vector<ll> ans;
    vector<char> target;
    cin >> N;

    // a ~ zのリストを生成
    for(moji='a'; moji<='z'; ++moji) {
        target.push_back(moji);
    }
    while(N != 0) {
        --N;
        ans.push_back(N % 26);
        N = N / 26;
    }

    int count = ans.size();
    for(int i = 0; i < count; ++i) {
        cout << target[ans.back()];
        ans.pop_back();
    } cout << endl;
    return 0;
}
