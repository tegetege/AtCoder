#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() { 
    int N, hh, mm, ss;
    cin >> N;
    hh = N / 3600;
    N -= 3600*hh;
    mm = N / 60;
    N -= 60*mm;
    ss = N;
    printf("%02d:%02d:%02d\n", hh, mm, ss);

    return 0;
}
