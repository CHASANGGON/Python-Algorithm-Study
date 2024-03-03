import sys
sys.stdin.readline

n = int(input())

arr = [[0]*101 for _ in range(101)]

for _ in range(n):
    x, y = map(int,input().split())
    
    