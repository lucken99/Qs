import sys
import collections


input = sys.stdin.readline

def solve(s, n, k):
    c = 0
    for i in range(n//2):
        if s[i] != s[n-i+1]:
            c += 1
    if c > k:
        return c-k
    return k-c

if __name__ == '__main__':
	for t in range(int(input())):
		n, k = map(int, input().strip().split())
		s = input().strip()
		print(f"Case #{t+1}:", solve(s, n, k))