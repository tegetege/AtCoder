#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
// 割り切れる素数を求める
// eは1が基本の初期値、ただしz = p^eがすでに存在している場合はe++する

int main() {
    int count;
    long long N;
    vector<long long> A(N);
    cin >> N;

    count = 0;
    while (true) {
        
        rep(i, A.size()) {
            if (A.at(i) == "hogehoge"){
                cout << count << endl;
                exit(0);
            }
        }
        count ++
    } 

}
