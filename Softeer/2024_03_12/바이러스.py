import sys
input = sys.stdin.readline

k, p, n = map(int,input().split())
a = k % 1000000007
b = p**n % 1000000007


print(a*b%1000000007)