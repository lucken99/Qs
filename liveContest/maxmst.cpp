#include <bits/stdc++.h>
using namespace std;

vector<int> parent, rank;

void make_set(int v) {
    parent[v] = v;
    rank[v] = 0;
}

int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
}

struct Edge {
    int u, v, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};
int main(){
    vector<Edge> edges;
    int n, d;
    cin >> n >> d;
    // cin >> d;

    // cout << n;
    int v[n][d]; 
    for (int i = 0; i<n; i++){
        for (int j=0; j< d; j++){
            cin >> v[i][j];
        }
    }
    // for (int i = 0; i<n; i++){
    //     for (int j=0; j< d; j++){
    //         cout << v[i][j];
    //     }
    //     cout << "\n";
    // }


    for (int i=0; i<n; i++){
        for (int j= i+1; j<n; j++){
            int sum = 0;
            for (int k=0 ;k<d; k++){
                sum += abs(v[i][k]-v[j][k]);
            }
            // w[i][j] = -sum;
            // w[j][i] = -sum;
            Edge e;
            e.u = i;
            e.v = j;
            e.weight = -1*sum;
            edges.push_back(e);
        }
    }

    int cost = 0;
    vector<Edge> result;
    parent.resize(n);
    rank.resize(n);
    for (int i = 0; i < n; i++)
        make_set(i);

    sort(edges.begin(), edges.end());

    for (Edge e : edges) {
        if (find_set(e.u) != find_set(e.v)) {
            cost += e.weight;
            result.push_back(e);
            union_sets(e.u, e.v);
        }
    }
    return 0;
}





