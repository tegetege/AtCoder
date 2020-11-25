// https://atcoder.jp/contests/atc001/tasks/unionfind_a
// B - Union Find
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define endl "\n"
int par[100000]; // 親
int rank_tree[100000]; // 木の深さ

// 初期化
void init(int N) {
    rep(i, N) {
        par[i] = i;
        rank_tree[i] = 0;
    } 
}

// 木の根を求める
int find(int x) {
    if (par[x] == x) {
        return x;
    } else {
        return par[x] = find(par[x]);
    }
}

// xとyの属する集合を併合
void unite(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y) return ;
    
    if (rank_tree[x] < rank_tree[y]){
        par[x] = y;
    } else {
        par[y] = x;
        if (rank_tree[x] == rank_tree[y]) rank_tree[x]++;
    }
}

// xとyが同じ集合に属するかどうか
bool same(int x, int y) {
    return find(x) == find(y);
}



int main() { 
    int N, Q, P, A, B;
    cin >> N >> Q;

    init(N); //初期化

    rep(i, Q) {
        cin >> P >> A >> B;
        if (P == 0) {
            unite(A, B);
        } else {
            if (same(A, B)) cout << "Yes" << endl;
            else cout << "No" << endl;
        }

    }
    return 0;
}
