# n, s,p,q= map(int, input().split())
# a = []
# a.append(s%2**31)
# for i in range(1,n):
# 	a.append((a[i-1]*p+q)%(2**31))

# print(len(set(a)));

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,s,p,q;
    cin >> n >> s >> p >> q;
    vector<int> a;
    a[0] = s%2147483648;
    for(int i=1;i<n;i++){
        a[i] = (a[i-1]*p+q)%(2147483648);
    }
    cout << a.size() << "\n";

    return 0;
}