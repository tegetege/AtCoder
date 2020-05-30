#include <bits/stdc++.h>
using namespace std;

int main() {
    string N,hon,pon,bon;

    cin >> N;
    hon = "2,4,5,7,9";
    pon = "0,1,6,8";
    bon = "3";
    if (hon.find(N.at(N.size()-1)) != string::npos) {
        cout << "hon" << endl;
    } else if (pon.find(N.at(N.size()-1)) != string::npos) {
        cout << "pon" << endl;
    } else {
        cout << "bon" << endl;
    }
}
