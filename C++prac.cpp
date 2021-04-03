#include <bits/stdc++.h>

using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);

	int testcases;
	cin >> testcases;
	while(testcases--){
		int n;
		cin >> n;
		vector<int> p(n);
		for (int i = 0; i < n; i++){
			cin >> p[i];
			--p[i];

		}
		for (int i = 0; i < n; i++){
			cout << p[i] << " ";
		}
		cout << '\n';
	}
}