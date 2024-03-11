def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < N
 
def dfs():
    global cnt
    
    while stack:
        i, j = stack.pop()
        cnt += 1
        arr[i][j] = 0 # 방문 체크

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 인덱스 검사 & 블록 검사 & 스택 중복 체크
            if in_range(ni,nj) and arr[ni][nj] and [ni,nj] not in stack:
                stack.append([ni,nj])



import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().rstrip())) for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

block_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt = 0
            stack = [[i,j]]
            dfs()
            block_lst.append(cnt) # 블록의 개수를 append

print(len(block_lst))
block_lst.sort()
for b in block_lst:
    print(b)