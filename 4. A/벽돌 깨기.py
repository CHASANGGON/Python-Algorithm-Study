T = int(input())

for tc in range(1,T+1):
    n, w, h = [list(map(int,input().split())) for _ in range(h)]
    brick = [list(map(int,input().split())) for _ in range(h)]
    
    # 1 ≤ N ≤ 4 -> 최대 12**4 case 다 구해보면 될 듯...
    # 남아있는 벽돌의 최솟값을 구하는 문제니까, 최솟값보다 더 작아지면 
    
    print(f'#{tc} {0}')