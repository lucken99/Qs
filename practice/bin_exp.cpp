#include <bits/stdc++.h>

using namespace std;

long binexpo(long long a, long long n)
{
	long long copy_n{ n };
	long long ans{ 1 };
	while(copy_n)
	{
		if (copy_n&1)
		{
			ans *= a;
		}
		a *= a;
		copy_n >>= 1;
	}

	return ans;
}

int main()
{	
	cout << binexpo(2, 63) << '\n';
	return 0;	
}