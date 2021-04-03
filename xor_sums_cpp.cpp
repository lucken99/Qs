#include <bits/stdc++.h>
using namespace std;
using mint = atcoder::modint998244353;
const int N = 200005;
mint fact[N];
void preprocess()
{
	fact[0] = 1;
	for (int i = 1; i <= N; i++) fact[i] = (fact[i-1] * mint(i));
}

mint ncr(int n, int r)
{
	if (n < r) return mint(0);
	mint num = fact[n];
	mint den = fact[n - r] * fact[r];
	return num / den;
}

int main()
{
	// boost();
	preprocess();
	int n;
	cin >> n;
	vector<int> a(n), c1(30), c0(30);
	for (auto &x: a)
	{
		cin >> x;
		for (int i = 0; i < 30; i++)
		{
			((1 << i)&x) ? c1[i]++ : c0[i]++;
		}
	}
	vector<mint> val(n + 1);
	for (int bit = 0; bit < 30; bit++)
	{
		int p = c0[bit], q = c1[bit];
		vector<int> f1(n + 1, 0), f2(n + 1, 0);

		for (int i = 0; i <= q; i++)
		{
			if (i & 1) f1[i] = ncr(q, i).val();
			else f1[i] = 0;
		}

		for (int i = 0; i <= p; i++) f2[i] = ncr(p, i).val();

		auto f3 = atcoder::convolution(f1, f2);
		for (int i = 0; i <= n; i++)
		{
			val[i] += (mint(2).pow(bit) * f3[i]);
		}

	}
	for (int i = 1; i <= n; i++)
	{
		val[i] += val[i-1];
	}

	int Q; cin >> Q;
	while (Q--)
	{
		int m; cin >> m;
		cout << val[m].val() << '\n';
	}

	return 0;
}