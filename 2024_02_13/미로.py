# 미로
# 도착지(3) -> 출발지(2)
T = int(input())

def new_func(i, j): # count 함수
    cnt = 0
    lst = []
    for k in range(4):
        if 0 <= i + di[k] < n and 0 <= j + dj[k] < n:
            if maze[i+di[k]][j+dj[k]] == '0' or maze[i+di[k]][j+dj[k]] == '2':
                lst.append(k)     
    return lst

for test_case in range(1,T+1):

    n = int(input())
    maze = [list(input().rstrip()) for _ in range(n)]
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    # 도착지 좌표 찾기
    for i in range(n):
        if '3' in maze[i]:
            break
    j = maze[i].index('3')


    # 도착지 주변의 길 개수 구하기
    lst = new_func(i, j) # 함수 호출

    # 모든 경로를 push
    # 그런 후에 방문한 곳을 모두 벽(1)으로 바꿔버리기
    founded = False
    for k in lst: # 경로의 시작 위치 잡아주기
        i += di[k]
        j += dj[k]
        
        stack = [] # 스택은 새로운 경로마다 초기화
        stack.append((i,j)) # 처음 위치 push
        
        while stack:
            maze[i][j] = '1' # 방문한 곳을 벽으로 바꿔버리기
            visitable = new_func(i,j) # 현재 위치에서 이동 가능한 델타 값 받기
            if visitable:
                for k in visitable: # 현재 위치에서 이동 가능한 곳 체크
                    ii = i + di[k]  # 이동 가능한 위치가 여러 개일 경우 모두 추가를 위해 임시 변수 설정
                    jj = j + dj[k]
                    if maze[ii][jj] == '2': # 미로 탈출
                        founded = True      # 출력 제어를 위한 변수
                        while stack: # while문 종료를 위해 스택 비우기
                            stack.pop()
                        break
                    stack.append((ii,jj)) # 이동 가능한 위치 모두 push
                i = ii # 가장 마지막 위치로 현재 위치를 갱신
                j = jj
            else:
                i, j = stack.pop() # 갈 수 있는 곳이 없으면 돌아가기
    
    if founded:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')