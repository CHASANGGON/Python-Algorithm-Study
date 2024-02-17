T = int(input())
for test_case in range(1, T+1):
    lst = [[0]*10 for _ in range(10)]
    N = int(input())
    purple = 0

    for _ in range(N):
        x1, y1, x2, y2, color = map(int,input().split())
        x1, x2 = min(x1,x2), max(x1,x2)
        y1, y2 = min(y1,y2), max(y1,y2)
    
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if lst[x][y] | color == 3:
                    purple += 1
                lst[x][y] = color

    print(f'#{test_case} {purple}')