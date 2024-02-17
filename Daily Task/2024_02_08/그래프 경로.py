T = int(input())

for test_case in range(1,T+1):
    # V와 E의 개수
    V, E = map(int,input().split())
    

    # node(node) 생성
    # node는 V의 개수만큼 생성
    # node에는 해당 node에서 인접한 다른 node 정보를 저장해야함
    # 그렇기에 2차원 리스트로 생성
    # 간선(edge)정보인 '0 1' 을 입력으로 받았다면
    # node[0].append(1) 를 실행
    # 그 결과 node = [ [1], [], [] ]
    # 즉, 위 결과의 의미는 node의 인덱스 0 에는 [1] 이 있고
    # 이 말은 node 0 에서 인접한 node는 1이라는 의미
    node = [[] for _ in range(V+1)] # V개를 생성한다고 했지만 node가 1부터 시작이라서 V+1 개 생성
    visited = [False]*(V+1) # 방문 체크를 위한 리스트
    stack = [] # 방문 가능한 node 저장을 위한 stack


    # Edge(간선) 정보 입력 받기
    # E 줄에 걸쳐, 출발 node-도착 node 입력
    # 이 문제는 한 쪽으로만 이동이 가능한 방향성 그래프
    # 그래서 start node에만 end를 추가
    # 양쪽으로 이동이 가능한 무방향성 그래프 였다면
    # end node에도 start를 추가
    # 또한 무방향성 그래프 였다면 모든 node끼리 방문 가능하므로 애초에 문제 성립 X
    for i in range(E):
        start, end = map(int,input().split())
        node[start].append(end)

    
    # 경로의 존재를 확인해야할 출발 node S와 도착 node G 입력 받기
    S, G = map(int, input().split())


    # 강의 자료를 찾아보면, DFS를 할 때 "종료 조건 = stack이 비워질 때"
    # 그 이유를 다시 떠올려보자면, stack의 후입선출(LIFO)구조에 따라서
    # stack에는 되돌아가기 위한 정보를 저장함
    # 더 깊은 node로 내려갈 때 stack에 push, 다시 올라올 때 pop
    # 그렇기에 stack에 아무것도 없다면 되돌아갈 node가 없다는 뜻!
    # 즉, 시작 node가 최상단이라면, 그래프에 존재하는 모든 node를 탐색하고,
    # 다시 최상단으로 돌아와서 종료하겠지만
    # 중간의 어떠한 node를 시작 node로 준다면, 시작 node 기준 아래의 모든 node를 탐색하고,
    # 더 이상 되돌아가지 못하므로 해당 위치에서(중간의 어떠한 node) 종료하게 된다.
    

    # 이 문제는 방향성 그래프이다
    # 그래서 출발 node S로 부터 도착 node G까지 도달할 수 있는지 여부를 판단한다.
    # 도착 node가 출발 node보다 위에 있다면 안 봐도 도달하지 못 할 것이고
    # 출발 node 기준에서 아래의 간선으로 도착 node가 없어도 도달하지 못 할 것이다.

    # 그렇기에 문제에서 요구하는 출발 node S와 도착 node G가 주어진다면
    # 나는 DFS(깊이 우선 (완전) 탐색) 코드에다가 시작 node를 S로 입력 해주기만 한다면,
    # 코드는 node S를 기준으로 아래에 존재하는 모든 node를 완전 탐색할 것이고
    # 모든 node를 탐색한 후 다시 출발 node S로 돌아온 상황에서는 stack이 비워져서 DFS를 종료하게 되고
    # 그 후 내가 확인하고자 하는 도착 node G가 방문 표시가 되어 있는지를 체크하면 된다.

    # 그런데 이 문제는 방문 과정(경로)을 하나하나 기억하거나 출력할 필요는 없으므로
    # 방문 가능한 node들을 stack에 push해서 저장한 후
    # 바로 다시 stack에서 pop해서 방문 체크를 한 후, 아래로 내려가기만 하고
    # 계속 내려가다가 더 이상 방문가능한 node가 없다면(stack이 비워졌다면)
    # 반복문을 종료하면 된다.
    
    # 바로 다시 stack에서 pop한다는 부분이 이해가 가지 않을 수 있는데,
    # 경로를 기억하거나 출력하면서 DFS하는 경우는
    # 아래로 내려가다가 더 이상 못내려간다면, 바로 위로 돌아가야 하므로 그 때만 pop을 한다.
    
    # 하지만 이 문제는 그냥 아래로 내려가기만 하면 되기에 방문 가능한 node들을 한 번에 모두 push하고
    # 그 push한 node들을 간선으로 이어져있는지 여부와는 상관없이 바로 pop해서 방문한다.
    # 문제의 그림으로 이해를 돕자면, 경로를 기억해야한다면
    # 1 -> 3 -> 1 -> 4 -> 6 -> 4 -> 1(종료) 이 순서대로 실행되겠지만
    # 이 문제는 1 -> 3 > 4 -> 6 이 순서로 끝나게 된다.
    # 즉, 굳이 되돌아가기 위한 pop을 하지 않고, 방문 가능한 node로 바로 순간이동(pop) 하면 된다고 보면된다.
    # 경로를 기억하는 코드로 해도 아무 문제는 없다. 다만 불필요하다는 말.


    # 시작 node를 출발 node S로 설정
    stack.append(S)

    while stack: # stack이 비워지면 탐색 종료
        now_v = stack.pop() # stack에서(방문 가능한 node 목록) 현재 node 꺼내오기
        visited[now_v] = True # 현재 node 방문 표시
        
        
        for next_v in node[now_v]: # 현재 node에서 방문 가능한 node 리스트 순회
                                     # test_case 1을 그림으로 이해하면 4, 3이 주어짐
            
            if not visited[next_v]: # (아직 방문하지 않은 & 방문 가능한) node 목록들을 stack에 추가
                stack.append(next_v)      
                                    # stack = [4,3] 인 상태로 for문 종료
                                    
                                    # while문이 새로 시작되면
                                    # pop한 결과 now_v = 3 이 되고
                                    # stack = [4]
                                    # node 3 에 방문체크후 for문을 반복하려고 하지만
                                    # node 3 에서는 방문 가능한 node 가 없으므로 바로 종료
                                    
                                    # while문이 새로 시작되면
                                    # pop한 결과 now_v = 4 가 되고
                                    # stack = []
                                    # node 4 에 방문체크후 for문을 반복
                                    # node 4 에서는 방문 가능한 node 가 6이 있어서
                                    # stack = [6]

                                    # while문이 새로 시작되고
                                    # 위의 과정과 동일하게 실행 결과 방문 가능한 node가 없으므로
                                    # append가 실행되지 않아서 stack은 비워져있고, while문이 종료됨

    # 주어진 시작 node S로부터 출발하여, 아래의 모든 node를 탐색한 결과,
    # 도착 node G까지 도달했다면, 도착 node G는 True로 바뀌어있을 것임 
    if visited[G] == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0') 