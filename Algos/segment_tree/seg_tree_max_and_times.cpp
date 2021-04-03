// Finding the maximum and number of times it appears.

/*	To solve this problem, we store a pair of numbers at each vertex in the tree:
 In addition to the maximum we also store the number of
 occurrences of it in the corresponding segment. 
 Determining the correct pair to store at t[v] can still be done in constant time using 
 the information of the pairs stored at the child vertices. 
 Combining two such pairs should be done in a separate function, 
 since this will be an operation that we will do while building the tree, 
 while answering maximum queries and while performing modifications.
	*/

#include <bits/stdc++.h>

using namespace std;

int n;
//int MAXN = n;
//int t[4*MAXN];
int INF = 100000000+7;

pair<int, int> t[4*12];

pair<int, int> combine(pair<int, int> a, pair<int, int> b){
	if (a.first > b.first)
		return a;
	if (b.first > a.first)
		return b;
	return make_pair(a.first, a.second + b.second);
}

void build(int a[], int v, int tl, int tr){
	if (tl == tr){
		t[v] = make_pair(a[tl], 1);
	} else{
		int tm = (tl + tr) / 2;
		build(a, v*2, tl, tm);
		build(a, v*2+1, tm+1, tr);
		t[v] = combine(t[v*2], t[v*2+1]);
	}
}

pair<int, int> get_max(int v, int tl, int tr, int l, int r){
	if (l > r)
		return make_pair(-INF, 0);
	if (l == tl && r == tr)
		return t[v];
	int tm = (tl + tr) / 2;
	return combine(get_max(v*2, tl, tm, l, min(r, tm)),
					get_max(v*2+1, tm+1, tr, max(l, tm+1), r));
}

void update(int v, int tl, int tr, int pos, int new_val){
	if (tl == tr){
		t[v] = make_pair(new_val, 1);
	} else {
		int tm = (tl + tr) / 2;
		if (pos <= tm)
			update(v*2, tl, tm, pos, new_val);
		else
			update(v*2+1, tm+1, tr, pos, new_val);
		t[v] = combine(t[v*2], t[v*2+1]);
	}
}

int main(){
	int a[] = {5,4,8,5 ,5,8, 8,8,5,4,7,6};
	build(a, 1, 0, 11);
	for (auto x: t){
		cout << x.first << " " << x.second << " ,";

	}
	cout << "\n";
	update(1, 0, 11, 4, 8);
	for (auto x: t){
		cout << x.first << " " << x.second << " ,";

	}
	
}