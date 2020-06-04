#include <bits/stdc++.h>
using namespace std;



int main() {
    int N;
    cin >> N;
    vector<int> vec(N);
    for (int i = 0; i < N; i++) {
        cin >> vec.at(i);
    }

    int ans = 0, ave = 0;
    for (int i = 0; i < N; i++) {
        ans += vec.at(i);
    }
    ave = (ans / N);

    for (int i = 0; i < N; i++) {

        if (vec.at(i) > ave) {
            cout << vec.at(i) - ave << endl;
        } else {
            cout << ave - vec.at(i) << endl;
         }
    }


}
