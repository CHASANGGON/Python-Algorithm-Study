import sys
input = sys.stdin.readline

arr = [[0]*1001 for _ in range(1001)]

N = int(input())

for n in range(1,N+1):
    sj, si, w, h = map(int,input().split())
    
    for i in range(si,si+h):
        for j in range(sj,sj+w):
            arr[i][j] = n
            
cnt_lst = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j]:
            cnt_lst[arr[i][j]] += 1

print(*cnt_lst[1:],sep='\n')