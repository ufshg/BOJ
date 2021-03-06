import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d1 = {}
d2 = {}

for i in range(n):
    temp = input().strip()
    d1[str(i + 1)] = temp
    d2[temp] = str(i + 1)

for _ in range(m):
    temp = input().strip()
    if temp in d1:
        print(d1[temp])
    else:
        print(d2[temp])