#include <bits/stdc++.h>
using namespace std;


int dp[4010][4010];
int box(int *arr, int buf1, int buf2, int n) {
    if (buf1 <= 0 && buf2 <= 0)
        return 0;
    if (n < 0)
        return 6000;

    if (buf1 <= 0 || buf2 <= 0) {
        if (buf1 <= 0) {
            if (dp[0][buf2] > 0)
                return dp[0][buf2];
            int x = 1 + box(arr, buf1, buf2 - arr[n], n - 1);
            dp[0][buf2] = x;
            return x;
        }
        if (buf2 <= 0) {
            if (dp[buf1][0] > 0)
                return dp[buf1][0];
            int x = 1 + box(arr, buf1 - arr[n], buf2, n - 1);
            dp[buf1][0] = x;
            return x;
        }
    }
    if (dp[buf1][buf2] > 0)
        return dp[buf1][buf2];
    int x = min(1 + box(arr, buf1 - arr[n], buf2, n - 1),
                1 + box(arr, buf1, buf2 - arr[n], n - 1));
    dp[buf1][buf2] = x;
    return x;
}
void solve() {
    long long int n, k;
    cin >> n >> k;
    int arr[n];
    for (long long int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    for (int i = 0; i <= 4005; i++)
        for (int j = 0; j <= 4005; j++)
            dp[i][j] = -1;
    int x = box(arr, k, k, n - 1);
    if (x > 5000)
        cout << -1 << "\n";
    else
        cout << x << "\n";
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}