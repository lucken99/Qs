/**
 *    author:  tourist
 *    created: 28.11.2020 17:49:32       
**/
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  while (tt--) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    vector<long long> pref(n);
    for (int i = 1; i < n; i++) {
      pref[i] = pref[i - 1] + a[i];
    }
    vector<long long> suf(n + 1);
    for (int i = n - 1; i >= 1; i--) {
      suf[i] = suf[i + 1] + a[i];
    }
    long long low = 0;
    long long high = (long long) 1e18;
    while (low < high) {
      long long mid = (low + high) >> 1;
      int L = 0;
      int R = n;
      long long mp = 0;
      long long ms = 0;
      while (L + 1 < R) {
        bool changed = false;
        while (L + 1 < R && pref[L + 1] + ms >= -mid) {
          mp = max(mp, pref[L + 1]);
          changed = true;
          L += 1;
        }
        while (L + 1 < R && suf[R - 1] + mp >= -mid) {
          ms = max(ms, suf[R - 1]);
          changed = true;
          R -= 1;
        }
        if (!changed) {
          break;
        }
      }
      if (L + 1 >= R) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    cout << min(a[0] - low, a[0] + pref[n - 1]) << '\n';
  }
  return 0;
}
