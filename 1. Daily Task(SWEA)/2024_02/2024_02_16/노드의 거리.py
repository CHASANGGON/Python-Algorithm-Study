
T = int(input())

for test_case in range(1,T+1):
    v, e = map(int,input().split()) # v 와 e 의 개수
    visited = [0]*(v+1)
    v = [[] for _ in range(v+1)]

    for _ in range(e): # 무방향 edge 정보
        start, end = map(int,input().split())
        v[start].append(end)
        v[end].append(start)
    
    start, end = map(int,input().split())

    distance = 0
    queue = [[start,distance]] # 큐 생성 및 출발노드 설정
    distance_lst = [] # 방문 가능한 노드의 거리 정보를 담을 리스트
    while queue:
        now_vertex,distance = queue.pop(0) # bfs로 현재 위치 갱신
        visited[now_vertex] = 1 # pop했을 때 방문 체크
    
        for connected_vertex in v[now_vertex]: # 현재 노드에서 연결된 노드 중에서
            if visited[connected_vertex] == 0:
                queue.append([connected_vertex,distance+1]) # 방문 가능한 노드만 queue에 추가
                distance_lst.append([connected_vertex,distance+1])

    if visited[end]: # 방문했으면
        for answer in distance_lst:
            if answer[0] == end: # 조사 대상인 node를 찾아서
                distance = answer[1] # 거리 정보를 변수에 저장
                break # for 문 탈출
    else:
        distance = 0

    print(f'#{test_case} {distance}')