import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().rstrip().split())
    s = input().rstrip()

    roper = 0
    for i in s:
        if i != 'a':
            roper += (123 - ord(i))
    if k == roper:
        print('a'*n)
    elif k > roper:
        print('a'*(n-1) + chr(ord('a') + (k-roper)%26))
    else:
        pass