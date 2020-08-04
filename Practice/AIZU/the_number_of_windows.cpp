// しゃくとり法(two pointers)
// 問題：http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp
// 参考：https://qiita.com/drken/items/ecd1a472d3a0e7db8dce

#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<long long> a(N),x(Q);
    rep(i, N) {
        cin >> a.at(i);
    }
    rep(i, Q) {
        cin >> x.at(i);
    }

    rep(i, Q) { // 各質問ごとに回していく
        long long res = 0; // 合計値

        int right = 0; // 考えている場所の右側の情報、使い回す
        long long sum = 0; // 考えている部分の合計値、使い回す
        for (int left = 0; left < N; ++left) {
            // 今考えているセルの次の値を入れても問題がなければすすむ
            while (right < N && sum + a[right] <= x[i]) {
                sum += a[right];
                ++right;
            }
            
            // while文をbreakしたところが条件を満たす最大のところ
            res += (right - left);

            if (right == left) {
                // leftはfor文で+1していくが、rightはしないので、
                // rightとleftが重なった場合は、ここで ++rightしてあげる必要がある
                ++right; 
            } else {
                // leftを +1するので、その分sumから引いておく
                sum -= a[left];
            }

        }
        
        cout << res << endl;
    }

    return 0;
}
