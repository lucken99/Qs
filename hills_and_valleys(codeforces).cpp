#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ll long long
#define vll vector<ll>
#define ld long double
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oset tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
#define osetll tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>
#define ook order_of_key
#define fbo find_by_order
const int MOD=1000000007; //998244353
long long int inverse(long long int i){
    if(i==1) return 1;
    return (MOD - ((MOD/i)*inverse(MOD%i))%MOD+MOD)%MOD;
}
ll POW(ll a,ll b)
{
    if(b==0) return 1;
    if(b==1) return a%MOD;
    ll temp=POW(a,b/2);
    if(b%2==0) return (temp*temp)%MOD;
    else return (((temp*temp)%MOD)*a)%MOD;
}
 
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        ll n;
        cin>>n;
        ll a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        ll c=0;
        ll p[n]={};
        for(int i=1;i<n-1;i++)
        {
            if(a[i]<a[i+1] && a[i]<a[i-1]) {c++; p[i]=1;}
            if(a[i]>a[i+1] && a[i]>a[i-1]) {c++; p[i]=1;}
        }
        ll mx=0;
        for(int i=1;i<n-1;i++)
        {
            if( (a[i]>a[i-1] && a[i]>a[i+1]) || (a[i]<a[i+1] && a[i]<a[i-1]))
            {
                ll k=0;
                ll temp=a[i-1];
                k++;
                if(p[i-1]==1) k++;
                if(p[i+1]==1) k++;
                if(i<n-2 && ((a[i+2]-a[i+1])*(temp-a[i+1]))>0 )
                {
                    k--;
                }
                mx=max(mx,k);
                
                k=0;
                temp=a[i+1];
                k++;
                if(p[i+1]==1) k++;
                if(p[i-1]==1) k++;
                if(i-2>=0 && ((a[i-2]-a[i-1])*(temp-a[i-1]))>0 )
                {
                    k--;
                }
                mx=max(mx,k);
            }
        }
        cout<<c-mx<<"\n";
    }
}