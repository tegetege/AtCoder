#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;
  int max_ = max(max(A,B),C);
  int min_ = min(min(A,B),C);
  cout << max_ - min_ << endl;

  return 0;
}
