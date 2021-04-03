#include <bits/stdc++.h>
using namespace std;
#define int long long
#define vi vector<int>
#define pb push_back
#define MOD 1000000007
void solve()
{
   int t;
   cin>>t;
   while(t--)
   {
       int n,c;cin>>n>>c;
       int w[n],p[n];
       for(int i=0; i<n;i++)
           cin>>w[i];
       for(int i=0; i<n;i++)
           cin>>p[i];
       multimap<double,int> mp;
       for(int i=0; i<n;i++) {
           mp.insert(make_pair((double)p[i]/w[i], i));
       }
       double result = 0;
       multimap<double,int>::reverse_iterator rev;
       for(rev = mp.rbegin(); rev != mp.rend();rev++) {

           double fraction = (double)c/w[rev->second];

           if(c >= 0 and w[rev->second] <= c) {
               result += p[rev->second];
               c -= w[rev->second];
           }
           else if(c < w[rev->second]) {
               result += fraction * p[rev->second];
               break;
           }
       }
       cout<< result % MOD <<"\n";
   }
}

int32_t main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    solve();
    return 0;
}
