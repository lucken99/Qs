# helphand
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

prime = SieveOfEratosthenes(1000006)
pre = [0]*(1000006)
for i in range(1,1000006):
    if prime[i]==True:
        pre[i] = 1+pre[i-1]
    else:
        pre[i] = pre[i-1]
dp = [0]*(1000006)
dp[1]=0
dp[2]=1
dp[3]=2
dp[4]=3

t= int(input())
for _ in range(t):
    n = int(input())
    if n==1:
        print(0)
    elif n==2:
        print(1)
    else:
        print(pre[n]-3+n)


# helphand
MAX = 1000001
prefix =[0]*(MAX + 1) 
  
def buildPrefix(): 
    prime = [1]*(MAX + 1) 
  
    p = 2
    while(p * p <= MAX):  
        if (prime[p] == 1): 
            i = p * 2
            while(i <= MAX): 
                prime[i] = 0
                i += p 
        p+=1
    for p in range(2,MAX+1):  
        prefix[p] = prefix[p - 1] 
        if (prime[p]==1): 
            prefix[p]+=1
 
def query(L, R): 
    return prefix[R]-prefix[L - 1]

t=int(input())
buildPrefix()
for i in range(0,t):
    n=int(input())
    if(n==1):
        print("0")
    elif(n==2):
        print("1")
    else:
        a=query(1,n)
        ans=((a-1)+(a-1)-1)+(n-a)
        print(ans)

# helphand
booprimes=[True]*(int(1e6)+1)
primes=[1]*(int(1e6)+1)
primes[0]=0 
primes[1]=0 
p=2
while p*p<=(int(1e6)):
    if booprimes[p]:
        for i in range(p*p,int(1e6)+1,p):
            booprimes[i]=False 
            primes[i]=0 
    p+=1 
#print(primes[:20])
for i in range(1,int(1e6)+1):
    primes[i]+=primes[i-1]
#print(primes[:20])
t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(0)
    elif n==2:
        print(1)
    else:
        print(primes[n]+n-3)



#special power strings
#include<bits/stdc++.h>
using namespace std;

set<char> s[3];

string u,v;

const int maxN=600;

int dp[maxN][maxN];

bool check(int i,int j)
{
    if(i==u.size() && j==v.size())
    {
        return true;
    }
    
    if(j==v.size())
    {
        return false;   
    }
    
    if(i==u.size())
    {
        if(v[j]=='#' || v[j]=='?' || v[j]=='!')
        {
            return check(i,j+1);
        }
        else
        {
            return false;
        }
    }
    
    if(dp[i][j]!=-1)
    {
        return dp[i][j];
    }
    
    bool ans=false;
    
    if(v[j]>='a' && v[j]<='z')
    {
        if(u[i]==v[j])
        {
            ans=check(i+1,j+1);
        }
    }
    
    if(v[j]=='#')
    {
        ans=check(i,j+1);
        
        if(s[0].count(u[i]))
        {
            ans|=check(i+1,j);
        }
    }
    
    if(v[j]=='?')
    {
        ans=check(i,j+1);
        
        if(s[1].count(u[i]))
        {
            ans|=check(i+1,j);
        }
    }
    
    if(v[j]=='!')
    {
        ans=check(i,j+1);
        
        if(s[2].count(u[i]))
        {
            ans|=check(i+1,j);
        }
    }
    
    dp[i][j]=ans;
    return ans;
}

int main()
{
    int t;
    cin>>t;
    
    while(t--)
    {
        string a,b;
        cin>>a>>b;
        
        string temp;
        
        for(int i=0;i<3;i++)
        {
            s[i].clear();
            
            cin>>temp;
            for(int j=0;j<temp.size();j++)
            {
                s[i].insert(temp[j]);
            }
        }
        
        u=a;
    
        bool flag=0;
        
        int mi=4;
        
        for(int i=0;i<8;i++)
        {
    
            bool f1=(i&1);
            bool f2=(i&2);
            bool f3=(i&4);
            
            string temp="";
            
            for(int j=0;j<b.size();j++)
            {
                if(b[j]>='a' && b[j]<='z')  
                {
                    temp.push_back(b[j]);
                }
                if(b[j]=='#' && f1)
                {
                    temp.push_back(b[j]);
                }
                if(b[j]=='?' && f2)
                {
                    temp.push_back(b[j]);
                }
                if(b[j]=='!' && f3)
                {
                    temp.push_back(b[j]);   
                }
            }
            
            v=temp;
            
            for(int i=0;i<u.size();i++)
            {
                for(int j=0;j<v.size();j++)
                    dp[i][j]=-1;
            }
            
            if(check(0,0))
            {
                mi=min(mi,f1+f2+f3);
            }
        }
        
        if(mi==4)
        {
            mi=-1;
        }
        cout<<mi<<' ';
    }
    
    return 0;
}









    
