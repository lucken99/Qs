// simplest query and modification > add

/*	We begin by considering problems of the simplest form: 
the modification query should add a number x to all numbers in the segment a[l…r].
 The second query, that we are supposed to answer, asked simply for the value of a[i].
To make the addition query efficient, we store at each vertex in the Segment Tree 
how many we should add to all numbers in the corresponding segment. 
For example, if the query "add 3 to the whole array a[0…n−1]" comes,
 then we place the number 3 in the root of the tree. 
 In general we have to place this number multiple to multiple segments,
  which form a partition of the query segment. 
  Thus we don't have to change all O(n) values, but only O(logn) many.

If now there comes a query that asks the current value of a particular array entry,
 it is enough to go down the tree and add up all values found along the way.
*/

 

void build(int a[], int v, int tl, int tr){
	if (tl == tr){
		t[v] = a[tl];
	} else {
		int tm = (tl + tr) / 2;
		build( a, v*2, tl, tm);
		build(a, v*2+1, tm+1, tr);
		t[v] = 0;
	}
}

void update(int v, int tl, int tr, int l, int r, int add){
	if (l > r)
		return;
	if (l == tl && r == tr){
		t[v] += add;

	} else{
		int tm = (tl + tr) / 2;
		update(v*2, tl, tm, l, min(r, tm), add);
		update(v*2+1, tm+1, tr, max(l, tm+1), r, add);
	}
}

int get(int v, int tl, int tr, int pos){
	if (tl == tr)
		return t[v];
	int tm = (tl + tr) / 2;
	if (pos <= tm)
		return t[v] + get(v*2, tl, tm, pos);
	else:
		return t[v] + get(v*2+1, tm+a, tr, pos);
}

