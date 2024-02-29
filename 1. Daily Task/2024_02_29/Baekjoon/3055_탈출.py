# 비어있는 곳은 '.'
# 물이 차있는 지역은 '*'
# 돌은 'X' 
# 비버의 굴은 'D'
# 고슴도치의 위치는 'S'

# * 물은 .을 향해서 BFS
# 고슴도치는 S 에서 D로 BFS
def find_start():
    for i in range(r):
        for j in range(c):
            if forest[i][j] == 'S':
                nq.append([i,j,'S',0])
            
def find_water():
    water_lst = []
    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                nq.append([i,j,'*',0])
    
def out_of_range(ni,nj):
    return 0 <= ni < r and 0 <= nj < c

def bfs(nq):
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    while nq:
        q = nq.copy()
        nq.clear()
        move = False
        while q:
            # 좌표, 대상, 시간
            i, j, o, t = q.popleft()

            # 델타 탐색
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                # 인덱스 검사
                if out_of_range(ni,nj):

                    # 물 bfs
                    if o == '*' and forest[ni][nj] == '.' or forest[ni][nj] == 'S':
                        forest[ni][nj] = '*'
                        nq.append([ni,nj,'*',t+1])
                    
                    # 고슴도치 bfs
                    elif o == 'S' and forest[ni][nj] == '.':
                        forest[ni][nj] = 'S'
                        nq.append([ni,nj,'S',t+1])
                        move = True
                    
                    # 비버굴 도착
                    elif o == 'S' and forest[ni][nj] == 'D':
                        print(t+1)
                        return
        if not move:
            print("KAKTUS")
            return


from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int,input().split())

forest = [list(input().rstrip()) for _ in range(r)]

nq = deque()

find_water() # 물을 먼저 enque 해야 한다!! 중요! 그래야 고슴도치가 물을 침범하지 않음
find_start()
bfs(nq)