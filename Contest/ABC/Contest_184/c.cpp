#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"

// 斜めは永遠に行けるので、グリッドを市松模様(白黒)にしたときに同じ色には
// 一手で移動できる

int solve() {
    int x1, x2, y1, y2;
    cin >> x1 >> y1;
    cin >> x2 >> y2;

    // 0手でいけるところ
    if (x1 == x2 && y1 == y2) return 0;
    // 1手でいけるところ
    if (x1+y1 == x2+y2) return 1;
    if (x1-y1 == x2-y2) return 1;
    if (abs(x1-x2)+abs(y1-y2) <= 3) return 1;
    // 2手でいけるところ
    if ((x1+y1)%2 ==(x2+y2)%2) return 2;
    if (abs(x1-x2)+abs(y1-y2) <= 6) return 2;
    if (abs((x1+y1)-(x2+y2)) <= 3) return 2;
    if (abs((x1-y1)-(x2-y2)) <= 3) return 2;
    return 3;
}

int main() { 
    cout << solve() << endl;
    return 0;
}
