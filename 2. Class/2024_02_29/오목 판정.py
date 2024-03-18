def judgment():

    for i in range(n): # row
        for j in range(n): # col

            # 현재 위치 검사
            if arr[i][j] == 'o':

                # 델타 제어
                for k in range(4):

                    # 해당 방향으로의 길이 변경
                    for l in range(1,6):
                        # 탐색 위치 변경
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        
                        # 인덱스 검사 및 오목 판정
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                            pass
                        else:
                            break

                    # 계속 'o'가 나왔으면, l을 제어하는 for문이 5까지 진행됐고, 오목 YES
                    if l == 5:
                        return 'YES'
    
    # 오목 판정을 하지 못 했다면, 오목 NO
    return 'NO'

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    # 델타 : 아래, 오른쪽, 대각선1, 대각선2
    di = [1,0,1,1]
    dj = [0,1,1,-1]

    arr = [list(input()) for _ in range(n)]

    print(f'#{tc} {judgment()}')