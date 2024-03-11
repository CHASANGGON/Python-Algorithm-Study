import sys
input = sys.stdin.readline

N = int(input())
course = [[] for _ in range(N)]

for i in range(N):
    n, s, e = map(int,input().split())
    course[n-1] = [s,e]
    
course.sort(key = lambda x : (x[1],x[0]))
allocation = [1]*N
NN = N
cnt = 0
while NN: # N개의 배정
    cnt += 1 # 강의실 개수 카운트
    lt_idx = allocation.index(1) # 강의실 배정이 안 된 가장 빠른 강의 찾기
    last_end_time = course[lt_idx][1] # 마지막 강의 끝나는 시간 저장
    allocation[lt_idx] = 0 # 배정 완료
    NN -= 1
    if NN == 0:
        break
    for i in range(N):
        # 아직 배정이 되지 않았으면서
        # 마지막 강의가 끝나는 시간보다, 시작시간이 늦거나 같게 시작하는 강의를
        if allocation[i] and last_end_time <= course[i][0]:
            allocation[i] = 0 # 배정하고            
            last_end_time = course[i][1] # 마지막 강의 끝나는 시간 갱신
            NN -= 1 # 1개 배정 완료

print(cnt)