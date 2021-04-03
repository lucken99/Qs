// n, b = map(int, input().split())
// if b > (n*(n+1))//2:
//     print(-1)
// elif b < 2*n-1:
//     print(-1)
// elif b == (n*(n+1))//2:
//     for i in range(n-1):
//         print(i+1, i+2)
// elif b == 2*n-1:
//     for i in range(1, n):
//         print(1, i+1)
// elif n >= 2:
//     s = (n*(n+1))//2
//     ans = [[i, i+1] for i in range(1, n)]
//     # print(ans)
//     act_s = s - b
//     i = 0
//     k = 1
//     while i < act_s:
//         l = -1
//         for j in range(k):
//             if i == act_s:
//                 break
//             ans[l][0] -= 1
//             l -= 1
//             i += 1
//         k += 1
//     for i, j in ans:
//         print(i, j)
//     # print(ans)

#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n{};
    long long b{};
    cin >> n >> b;
    long long s{(n*(n+1))/2};

    if ((b > s) || (b < 2*n-1))
        cout << -1 << '\n';
    else if (b == s)
        for (long i = 0; i< n-1; i++)
            cout << i+1 << " " << i+2 << '\n';
    else if (b == 2*n-1)
        for (long i = 1; i < n; i++)
            cout << 1 << " "<< i+1 << '\n';
    else if (n >= 2){
        long ans[n][2];
        for (long i = 1; i< n; i++){
            ans[i][0] = i;
            ans[i][1] = i+1;
        }

        long long act_s = s - b;
        long long i = 0;
        long long k = 1;

        while (i < act_s){
            long long l = n-1;
            for ( long j = 0; j < k; j++ ){
                if (i == act_s)
                    break;
                ans[l][0]--;
                l--;
                i++;
            }
            k++;

        }
        for (long i=1; i<n;i++){
            cout << ans[i][0] << " "<< ans[i][1] << '\n';
        }

    }
}