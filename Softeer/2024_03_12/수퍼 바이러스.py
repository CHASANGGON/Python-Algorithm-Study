import sys
input = sys.stdin.readline

k, p, n = map(int,input().split())
print(k*(pow(p,n*10,1000000007))%1000000007)