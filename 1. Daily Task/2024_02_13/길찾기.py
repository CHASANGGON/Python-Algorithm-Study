def check(v):
    visited[v] = True # 방문 체크
    for next_node in edges[v]: # 갈 수 있는 길을 for문을 통해 모두 방문
        check(next_node) # 재귀로 방문

for test_case in range(1,11):
    t, n = map(int,input().split()) # test_case, 길의 총 개수
    temp = list(map(int,input().split())) # edge 정보를 리스트에 임시 저장
    edges = [[] for _ in range(100)] # 출발점은 0, 도착점은 99
    visited = [False]*100

    for i in range(n): # edge 정보 등록
        edges[temp[i*2]].append(temp[i*2+1])
    
    

    check(0)
    print(f'#{test_case} ',end='')
    if visited[99]:
        print(1)
    else:
        print(0)