import sys
input = sys.stdin.readline

n = int(input())

cnt_lst = [0]*10000000001

for _ in range(n):
    a, s, e = map(int,input().split())
    


print(max(cnt_lst))       