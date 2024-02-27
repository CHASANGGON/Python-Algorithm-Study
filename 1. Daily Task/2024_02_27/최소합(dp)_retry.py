# dp로 푸는 문제
# dp문제들의 접근 방법은 n일 때의 경우의 수가 어떻게 만들어지는지에 집중!!
# 이 문제에서 이동방향은 오른쪽과 아래로 한정돼 있음
# 그러므로 이 문제의 n은 바로 왼쪽과 위에서 오는 두 경우만 존재
# 최솟값을 구해야 하므로, 바로 왼쪽과 위의 값 중 더 작은 값을 고르면 됨
# 그렇게 하기위한 전제조건은 왼쪽과 위의 테두리 영역의 값이 모두 결정되면 된다.
# 따라서 배열의 왼쪽과 위의 테두리 영역을 완성시켜주고 dp를 구해주면 된다.

t = int(input())

for tc in range(1,t+1):
    
    n  = int(input())
    
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    # left & up 테두리 완성해주기
    for i in range(n-1):
        arr[i+1][0] += arr[i][0]
        arr[0][i+1] += arr[0][i]
    
    # 나머지 영역에 대해서 dp 수행
    for i in range(1,n):
        for j in range(1,n):
            arr[i][j] += min(arr[i-1][j], arr[i][j-1])
            
    print(f'#{tc} {arr[n-1][n-1]}')