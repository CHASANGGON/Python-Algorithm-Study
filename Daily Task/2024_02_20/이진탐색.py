# inorder traversal의 순서 = binary search의 값이 채워지는 순서
# Left Vertex Right
def inorder(now_vertex):
    global order # 순서를 기억해야 하므로 global 선언
    
    if left[now_vertex]: # left 간선이 존재하면 계속 내려간다
        inorder(left[now_vertex])
    
    # 왼쪽 끝에 도달했을 때, 간선이 없으므로 if문의 다음 부분이 드디어 실행된다.
    order += 1
    value[now_vertex] = order
    # 첫 실행에서, value[4] = 1 이 실행
    # 즉, 4번 node가 첫 번째 순서라는 말
    
    
    # 우측 간선이 없어서 재귀를 복귀한다.
    if right[now_vertex]:
        inorder(right[now_vertex])

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    
    # 간선 정보를 저장
    left = [0]*(n+1) 
    right = [0]*(n+1)
    
    # 값 정보를 저장
    value = [0]*(n+1)
    
    # 완전 이진 트리 생성(n까지 간선 정보를 입력하는 과정)
    for i in range(2,n+1):
        if i%2 == 0:
            left[i//2] = i # 1(i//2)번 노드는 2(i)번 노드와 연결
        else:
            right[i//2] = i # 1(i//2)번 노드는 3(i)번 노드와 연결
    order = 0
    inorder(1)
    print(f'#{test_case} {value[1]} {value[n//2]}')