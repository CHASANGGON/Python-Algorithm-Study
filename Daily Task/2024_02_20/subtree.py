T = int(input())

for test_case in range(1,T+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    
    # 간선 정보를 담을 리스트 생성
    # 노드 번호는 1번부터 E+1번까지 존재
    left = [0]*(E+2)
    right = [0]*(E+2)
    
    # 간선 정보 입력
    for i in range(E):
        if left[arr[2*i]]:
            right[arr[2*i]] = arr[2*i+1]
        else:
            left[arr[2*i]] = arr[2*i+1]
    
    stack = [right[N],left[N]]
    
    cnt = 1
    while stack:
        next_node = stack.pop(0)
        if next_node:
            cnt += 1
            stack.append(left[next_node])
            stack.append(right[next_node])
    
    print(f'#{test_case} {cnt}')