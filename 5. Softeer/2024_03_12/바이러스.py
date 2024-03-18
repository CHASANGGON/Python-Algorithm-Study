import sys
input = sys.stdin.readline

k, p, n = map(int,input().split())
a = k*p
for _ in range(n-1):
    a = (a*p) % 1000000007

print(a%1000000007)