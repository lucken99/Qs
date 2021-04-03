// #include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin >> n;
	for (int i=10; i>0; i--){
		if (n%i == 0){
			cout << i << '\n';
			break;
		}
	}
	return 0;
}

// n = int(input())
// for i in range(10, 0, -1):
// 	if n%i ==0:
// 		print(i)
// 		break
