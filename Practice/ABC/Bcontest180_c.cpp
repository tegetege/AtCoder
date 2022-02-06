#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 1; i <= (double)(n); i++)
#define endl "\n"

int main() { 
    ll N;
    vector<ll> que_a;
    deque<ll> que_b;
    cin >> N;
    double target = pow(N, 0.5);
    for(ll i=1; i*i <= N; ++i) {
        if (N % i == 0) {
            if (N / i != i) {
                que_a.push_back(i);
                que_b.push_front(N/i);
            } else {
                que_a.push_back(i);
                break;
            }
        } 
    }
    for (const auto& e: que_a) {
        cout << e << endl;
    }
    for (const auto& e: que_b) {
        cout << e << endl;
    }

    return 0;
}
