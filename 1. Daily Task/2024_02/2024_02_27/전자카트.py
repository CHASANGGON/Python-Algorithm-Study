# 1 -> 2 ~ n -> 1
# 2 ~ n -> 순열 생성
# [ 1 + 생성된 순열 + 1]
# 배열들의 합을 구한 후 최솟값 구하면 끝

# 계산
def calculation(P, n):
    path = [1] + P + [1]
    
    consumption = 0

    for i in range(n+1):
        consumption += arr[path[i]-1][path[i+1]-1]

    consumption_lst.append(consumption)

# 순열 생성 함수
def permutation(i,n):
    if i == n:
        calculation(P, n)
    else:
        for j in range(i,n):
            P[i], P[j] = P[j], P[i]
            permutation(i+1,n)
            P[i], P[j] = P[j], P[i]



t = int(input())

for tc in range(1,t+1):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]

    P = list(range(2,n+1))

    consumption_lst = []
    permutation(0,n-1)
    
    print(f'#{tc} {min(consumption_lst)}')