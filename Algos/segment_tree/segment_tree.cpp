// we store the segment tree simply as an array t[] with a size of 
// 4 times the input size n
#include <bits/stdc++.h>
using namespace std;

int n = 5;
int MAXN = n;

int t[20];

// procedure for constructing the Segment Tree from array a[]:
/* it is a recursive function with the parameters a[](the input array), 
   v(the index of the current vertex), and the boundaries tl and tr
   of the current segment	*/


void build(int a[], int v, int tl, int tr){
	if (tl == tr){
		t[v] = a[tl];
	} else {
		int tm = (tl + tr) / 2;
		build(a, v*2, tl, tm);
		build(a, v*2+1, tm+1, tr);
		// for sum query
		t[v] = t[v*2] + t[v*2+1];
		// for max query
		// t[v] = max(t[v*2], t[v*2+1]);
	}
}

// function for answering sum queries
/*
	v(current vertex), boundaries tl and tr, boundaries of the query l and r.	*/

int sum(int v, int tl, int tr, int l, int r){
	if (l > r)
		return 0;
	if (l == tl && r == tr){
		return t[v];

	}
	int tm =(tl + tr) / 2;
	// for sum
	return sum(v*2, tl, tm, l, min(r, tm))
			+ sum(v*2+1, tm+1, tr, max(l, tm+1), r);

	// for max
	// return max(sum(v*2, tl, tm, l, min(r, tm)),
	// 			sum(v*2+1, tm+1, tr, max(l, tm+1), r));
}


// the update query function
// v(current vertex), boundaries tl and tr, posiion and new_val

void update(int v, int tl, int tr, int pos, int new_val){
	if (tl == tr){
		t[v] = new_val;
	} else{
		int tm = (tl + tr) / 2;
		if (pos <= tm)
			update(v*2, tl, tm, pos, new_val);
		else
			update(v*2+1, tm+1, tr, pos, new_val);
		// for sum
		t[v] = t[v*2] + t[v*2+1];

		// for max
		// t[v] = max(t[v*2], t[v*2+1]);
	}
	//cout << t[0];
}

int main(){
	int a[] = {1, 3, -2, 8, -7};
	//int n = a.size();

	build(a, 1, 0, n-1);
	for (auto x: t){
		cout << x << " " ;
	}
	cout << "\n";
	update(1, 0, n-1, 2, 3);
	sum(1, 0, n-1, 2, 4);
	for (auto x: t){
		cout << x << " " ;
	}
	
}