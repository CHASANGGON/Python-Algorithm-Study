import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x : (x[0],x[1]), reverse=True)

for i in range(n):