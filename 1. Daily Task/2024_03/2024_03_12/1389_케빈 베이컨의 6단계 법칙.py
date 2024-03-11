def bfs():
    global cnt
    
    while dq:
        now_v, step = dq.popleft() # bfs를 위해 popleft
        
        for next_v in edge[now_v]: # 현재 노드에서 방문 가능한 노드 중에서
            if visited[next_v]: # 아직 방문하지 않았다면
                visited[next_v] = 0 # 방문 체크
                cnt += step # 단계 누적합
                dq.append([next_v,step+1]) # 1단계 추가 후 enque
                
                
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

edge = [[] for _ in range(n+1)] # 사람의 번호는 1부터 N

for _ in range(m):
    s, e = map(int,input().split())
    # A와 B가 친구이면, B와 A도 친구 = 양방향 그래프
    edge[s].append(e)
    edge[e].append(s)
    
kevin_bacon = [0]*(n+1)

for start_v in range(1,n+1):
    visited = [1]*(n+1) # 방문 정보 생성
    visited[start_v] = 0 # 시작 노드는 방문 대상에서 제외
    cnt = 0
    dq = deque()
    dq.append([start_v,1]) # 시작 노드와 단계 정보
    bfs()
    kevin_bacon[start_v] = cnt

min_human = min(kevin_bacon[1:])
num = kevin_bacon.index(min_human)
print(num)