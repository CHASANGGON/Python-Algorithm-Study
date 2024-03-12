def in_range(ni,nj):
    return 0 <= ni < n and 0 <= nj < n

def dfs():
    global cnt

    while stack:

        i, j = stack.pop()
        arr[i][j] = 0
        cnt += 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if in_range(ni,nj) and arr[ni][nj] and [ni,nj] not in stack:
                stack.append([ni,nj])



import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().rstrip())) for _ in range(n)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            cnt = 0
            stack = [[i,j]]
            dfs()
            lst.append(cnt)

print(len(lst))
lst.sort()
for l in lst:
    print(l)