import sys
input = sys.stdin.readline

n, l = map(int,input().split())

t = 0 # 시간
nd = 0 # 위치

for _ in range(n):
    d, r, g = map(int,input().split())
    
    t += (d-nd) # 신호등까지 이동 시간 누적
    nd = d # 위치 갱신
    
    rg_t = t % (r + g)
    if r - rg_t > 0:
        t += (r - rg_t)

t += (l-nd) # 마지막 신호등 위치에서 도로끝까지의 거리 누적
    
print(t)