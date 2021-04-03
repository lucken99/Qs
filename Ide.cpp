#include <bits/stdc++.h>
using namespace std;
#define int long long
#define vi vector<int>
#define pb push_back
#define MOD 1000000007
void solve()
{
    int t;cin>>t;
    while(t--) {
          int n;
    cin>>n;
    int a[n];
    for(int i=0 ;i<n;i++)
        cin>>a[i];
    int result =0;
    for(int i=0 ;i<n;i++) {
        result += floor(log10(a[i])) +1;
    }
    bool flag = false;
    int e = sqrt(result);
    for(int i=2 ; i<=e; i++){
        if(result % i == 0) {
            flag = true;
            break;
        }
    }
    if(flag) {
        cout<<"No\n";
    }
    else{
        cout<<"Yes\n";
    }
    }
}

int32_t main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    solve();
    return 0;
}
