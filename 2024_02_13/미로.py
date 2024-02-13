# 미로
# 도착지(3) -> 출발지(2)
T = int(input())

def new_func(i, j): # count 함수
    cnt = 0
    lst = []
    for k in range(4):
        if 0 <= i + di[k] < n and 0 <= j + dj[k] < n:
            if maze[i+di[k]][j+dj[k]] == '0':
                lst.append(k)     
    return lst

for test_case in range(1,T+1):

    n = int(input())
    maze = [input().rstrip() for _ in range(n)]
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    # 도착지 좌표 찾기
    for i in range(n):
        if '3' in maze[i]:
            break
    j = maze[i].index('3')


    # 도착지 주변의 길 개수 구하기
    lst = new_func(i, j) # 함수 호출
    cnt = len(lst) # 길의 개수


    # stack이 비워질 때 종료한다고 하면, 한 쪽길 밖에 생각 못해서 틀림
    # 음.. 그래서 출발지 주변에 길이 몇 개인지 cnt를 해야할 듯? 그리고 그만큼 매번 고려해봐야 할 듯
    # 도착지(3) 근처에 0이 몇 개인지 확인 -> cnt
    # while cnt : 안에 stack
    #  stack = [] -> 매번 초기화
    #   while stack: 갈 곳이 없어서 원위치로 돌아오면(stack이 비워지면 종료~)
    for k in lst: # 시작 위치 잡아주기
        ii, jj = di[k], dj[k]
        stack = [] # 스택은 길마다 초기화
        
        while stack:
            if len(new_func(ii, jj)) == 2:
            break