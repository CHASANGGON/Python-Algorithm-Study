T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    # 일차원 리스트에 간선 정보를 저장
    arr = [0]*(n+1)
    nums = list(map(int,input().split()))
    for i in range(1,n+1):
        arr[i] = nums[i-1] # 일차원 배열에 저장 -> 짝수 left, 홀수 right
        
        # 부모가(i//2) 자식보다(i) 크면 교환
        while arr[i//2] > arr[i]:
            arr[i//2], arr[i] = arr[i], arr[i//2]
            i //= 2
    
    s = 0   # 합을 저장할 방법
    n //= 2 # 본인 노드를 제외한 조상 노드만 고려
            # 일차원 배열에 간선정보를 저장했을 때
            # 조상을 찾아가는 방법 : n(완전 이진 트리에서 순서) // 2
            
    while n: # 0번 인덱스를 제외하고 조상을 찾아가며 모두 누적합
        s += arr[n]
        n //= 2
    print(f'#{test_case} {s}')