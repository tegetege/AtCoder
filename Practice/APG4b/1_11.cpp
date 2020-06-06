#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, B, i, c = 1;
    cin >> N >> A;
    vector<int> num(N+10);
    vector<string> op(N+10);
    for (i = 0; i < N; i++) {
        cin >> op.at(i) >> num.at(i);
    }
    // cout << op.at(0) << num.at(0) << endl;
    for (i = 0; i < N; i++) {
        if (op.at(i) == "+") {
            A += num.at(i);
        } else if (op.at(i) == "-") {
            A -= num.at(i);
        } else if (op.at(i) == "*") {
            A *= num.at(i);
        } else if (op.at(i) == "/" && num.at(i) != 0) {
            A /= num.at(i);
        } else if (op.at(i) == "/" && num.at(i) == 0) {
            cout << "error" << endl;
            return 0;
        }
        cout << c << ":" << A << endl;
        c++;
    }
}
