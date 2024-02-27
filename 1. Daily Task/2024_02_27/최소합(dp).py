# 해당 경로까지 갈 수 있는 최소 경로는
# 바로 윗칸 또는 왼쪽칸 중에서 더 작은 값을 가지는 칸에서 오는 것이다.
# 그러니까 우선은 그러한 계산이 가능하게 하기 위해 테두리 칸들을 계산한다.
# 테두리 칸은 최소로 가능한 방법이 따로 없이 그냥 직선으로 가면 된다.
# 그 후에 (1.1)부터 (n-1,n-1)까지 윗칸 또는 왼쪽칸 중 최소 값을 골라서 가면 된다.
# 이 때 반복되는 연산은 없기 때문에 이 문제의 알고리즘 분류는 dp다.

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]

    for i in range(n-1):
        arr[0][i+1] += arr[0][i]
        arr[i+1][0] += arr[i][0]

    for i in range(1,n):
        for j in range(1,n):
            arr[i][j] = min(arr[i-1][j],arr[i][j-1]) + arr[i][j]

    print(f'#{tc} {arr[n-1][n-1]}')