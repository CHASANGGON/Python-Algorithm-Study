from pprint import pprint
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 육지를 만나면 모든 육지를 탐색
#   탐색하면서 섬에 번호를 부여 
#       테두리의 좌표들을 저장
#           탐색이 끝나면 모은 좌표들을 저장

# 해당 과정을 끝내면 하나씩 꺼내서 bfs

collection_of_start_lines = []
land_num = 2
for i in range(n): # 완탐
    for j in range(n):
        if arr[i][j] == 1: # 육지라면
            arr[i][j] = land_num # 육지 번호 부여
            
            start_lines = []
            stack = [[i,j]]
            while stack: # dfs
                i,j = stack.pop()
                
                for ni, nj in (i+1,j), (i-1,j), (i,j+1), (i,j-1): # 델타 탐색
                    if 0 <= ni < n and 0 <= nj < n: # 인덱스 검사
                        if arr[ni][nj] == 1: # 육지면
                            arr[ni][nj] = land_num # 육지 번호 표시
                            stack.append([ni,nj]) # 다음 탐색을 위해 스택에 추가
                            
                        elif arr[ni][nj] == 0 and [ni,nj] not in start_lines: # 육지와 인접한 바다라면 추가 및 중복 제거
                            start_lines.append([ni,nj])
            
            land_num += 1 # 육지 번호 증가
            collection_of_start_lines.append(start_lines) # 컬렉션에 추가

min_length = 200 # 100*100 이니까 최댓값 200으로 설정
land_num = 2 # 육지 번호 초기화
for start_lines in collection_of_start_lines: # 컬렉션의 개수 만큼 탐색
    dq = deque()
    for i,j in start_lines:
        arr[i][j] = land_num # 방문표시
        dq.append([i,j,1]) # dq에 옮기기
        
    while dq:
        i,j,l = dq.popleft()
        for ni,nj in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 0: # 아직 방문한 적 없다면
                    arr[ni][nj] = land_num # 방문 표시
                    dq.append([ni,nj,l+1]) # 큐에 추가
                    
                # start_lines를 한 번 반복할 때 마다 land_num은 계속 증가시킴
                # -> land_num 보다 작은 값은 이미 방문한 적 있으므로 확인할 필요 없음
                elif arr[ni][nj] > land_num:
                    min_length = min(min_length, l)
                    dq = deque() # bfs 이므로 최단 거리로 도달한 상태이므로 바로 종료 -> 다음 start_lines 확인
    
    land_num += 1
    
print(min_length)
# pprint(arr)
# pprint(collection_of_start_lines)
# pprint(len(collection_of_start_lines))