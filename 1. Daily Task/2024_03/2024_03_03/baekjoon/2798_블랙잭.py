import sys
input = sys.stdin.readline

n, m = map(int,input().split())
card = list(map(int,input().split()))

max_s = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s = card[i] + card[j] + card[k]
            if s <= m and s > max_s:
                max_s = s

print(max_s)