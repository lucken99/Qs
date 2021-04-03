// Adding on segments, querying for maximum

// for each vertex of the segment Tree we have to store the maximum
// of the corresponding subsegment.
//the intersting part  is how to recompute hese values during modificaion request.

/*	For this purpose we keep store an additional value for each vertex. 
this value we store the addends we haven't propagated to the child vertices. 
Before traversing to a child vertex, we call push and propagate the value to both children.
 We have to do this in both the update function and the query function.	
 */

#include <bits/stdc++.h>

using namespace std;

int INF = 1000000007;

int t[24]; 
int lazy[24];

void push(int v){
	t[v*2] += lazy[v];
	lazy[v*2] += lazy[v];
	t[v*2+1] += lazy[v];
	lazy[v*2+1] += lazy[v];
	lazy[v] = 0;
}

void update(int v, int tl, int tr, int l, int r, int addend){
	if (l > r)
		return;
	if (l == tl && r == tr){
		t[v] += addend;
		lazy[v] += addend;
	} else {
		push(v);
		int tm = (tl + tr) / 2;
		update(v*2, tl, tm, l, min(r, tm), addend);
		update(v*2+1, tm+1, tr, max(l, tm+1), r, addend);
		t[v] = max(t[v*2], t[v*2+1]);
	}
}

int query(int v, int tl, int tr, int l, int r){
	if (l > r)
		return -INF;
	if (l <= tl && tr <= r)
		return t[v];
	push(v);
	int tm = (tl+tr) / 2;
	return max(query(v*2, tl, tm, l, min(r, tm)),
			query(v*2+1, tm+1, tr, max(l, tm+1), r));
}

void build(int a[], int v, int tl, int tr){
	if (tl == tr){
		t[v] = a[tl];
	} else {
		int tm = (tl + tr) / 2;
		build(a, v*2, tl, tm);
		build(a, v*2+1, tm+1, tr);
		t[v] = max(t[v*2], t[v*2+1]);
	}
}

int main(){
	int ans;
	int a[] = {1,5,1,2,1,5};
	build(a, 1, 0, 5);

	for (auto x : t){
		cout << x << " ";
	}
	cout << "\n";
	update(1, 0, 5, 0, 5, 2);
	update(1, 0, 5, 3, 5, 10);

	for (auto x : t){
		cout << x << " ";
	}
	cout << "\n";
	ans = query(1, 0, 5, 3, 5);
	cout << ans;

	// for ( auto x: lazy){
	// 	cout << x << " " ;
	// }
	int l[5] = {0};
	for (auto x : l){
		cout << x << " ";
	}


}