#include <iostream>
#include <math.h>
using namespace std;
int subSetXORSum(int arr[], int n) {
   int bitOR = 0;
   for (int i=0; i < n; ++i)
   bitOR |= arr[i];
   return (bitOR * pow(2, n-1));
}
int main() {
   int arr[] = {1, 3, 5, 2};
   int size = sizeof(arr) / sizeof(arr[0]);
   cout<<"Sum of XOR of all possible subsets is "<<subSetXORSum(arr, size);
}