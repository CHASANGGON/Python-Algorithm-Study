# 전자키트 retry
# 최소 소비량이니까 기저 조건에 도달하면 min값을 갱신
# + 중간에 백트래킹

# 기본은 순열을 생성하는 것
# 거기에 출발 위치가 0으로 고정이라는 점과
# 도착위치도 0으로 고정이라는 점 -> 길이도 1개 추가
# 나머지는 동일하다!

def f(i,s):
    global min_s

    if i == n:
        # print(p)
        s += arr[p[i-1]][p[0]]
        if s < min_s:
            min_s = s
    
    # 백트래킹
    if s >= min_s:
        return 

    else:
        for j in range(i,n):
            p[i], p[j] = p[j], p[i]
            f(i+1,s+arr[p[i-1]][p[i]])
            p[i], p[j] = p[j], p[i]

t = int(input())

for tc in range(1,t+1):

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    min_s = 99999 # 최솟값 변수 초기화
    p = list(range(n)) # permutation

    f(1,0) # 출발지는 0으로 확정이라서

    print(f'#{tc} {min_s}')