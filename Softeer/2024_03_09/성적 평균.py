import sys
input = sys.stdin.readline

n, k = map(int,input().split())
score = list(map(int,input().split()))
for _ in range(k):
    a, b = map(int,input().split())
    print('{:.2f}'.format(sum(score[a-1:b])/(b-a+1)))