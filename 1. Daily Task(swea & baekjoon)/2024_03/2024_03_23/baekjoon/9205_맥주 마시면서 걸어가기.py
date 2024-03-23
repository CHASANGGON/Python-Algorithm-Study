import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input()) # 편의점의 개수
    node = []
    start_i, start_j = map(int, input().split()) # 집
    for _ in range(n):
        i, j = map(int, input().split()) # 편의점
        node.append([i, j, 1]) # 좌표, not visit
    rock_i, rock_j = map(int, input().split()) # 락페스티벌


    stack = []
    stack.append([start_i, start_j])
    result = 'sad'

    while stack:
        now_i, now_j = stack.pop()
        if abs(now_i - rock_i) + abs(now_j - rock_j) <= 1000: # 현재 위치에서 도착할 수 있으면 탈출
            result = 'happy'
            break
        
        for i in range(n):
            if node[i][2] and abs(now_i - node[i][0]) + abs(now_j - node[i][1]) <= 1000: # 방문 가능하면
                    stack.append([node[i][0], node[i][1]])
                    node[i][2] = 0
    
    print(result)