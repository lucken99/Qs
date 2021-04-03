#include <bits/stdc++.h>

// using namespace std;

int highestPowerof2(int n) 
{ 
   int p = (int)std::log2(n); 
   return (int)std::pow(2, p);  
} 

int main(){
	int t{};
	std::cin >> t;
	while (t--){
		int x{};
		int n{};
		std::cin >> n >> x;
		int a[n] {};
		for(int i=0; i<n; i++){
			std::cin >> a[i];
		}

		int z{1}, i{0};
		while ((z <= x) && (i < n)){
			if (a[i] == 0){
				i++;
				continue;
			}
			int p {highestPowerof2(a[i])};
			for (int j=i+1; j<n; j++){
				if (a[j]^p < a[j]){
					a[j] ^= p;
					a[i] ^= p;
					z++;
					break;
				}
				else if (j == n-1){
					a[j] ^= p;
					a[i] ^= p;
					z++;
					break;
				}
			}
			if (i == n-1)
				break;
		}
		int r{0};
		r = x - z;
		if (r && n==2){
			if (r&1){
				a[0] = 1;
				a[1] ^= 1;
			}

		}
	for(int i=0; i<n; i++){
		std::cout << a[i] << " ";
	}
	std::cout << '\n';
	}
}