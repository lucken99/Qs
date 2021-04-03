#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t{};
	cin >> t;
	while (t--)
	{
		int n{};
		cin >> n;
		vector<long> a(n);
		for (int i=0; i< n; i++)
		{
			cin >> a[i];
		}
		int ans{};
		for (int i = 0; i< n; i++)
		{
			if ((a[i]%2) == 0)
				ans++;
			long x = a[i];
			for (int j = i+1; j < n; j++)
			{
				long z = x^a[j];
				if ((z%2)==0)
					ans++;
				x = z;
			}
		}
		cout << ans << '\n';
	}
}