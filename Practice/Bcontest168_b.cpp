#include <bits/stdc++.h>
using namespace std;

int main() {
    int K;
    string N;
    cin >> K;
    cin >> N;

    if (N.size() <= K ) {
        cout << N << endl;
    } else {
        cout << N.erase(K) + "..." << endl;
    }

}
