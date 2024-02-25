t = int(input())

for tc in range(1,t+1):
    n = int(input())
    balloon = [list(map(int,input().split())) for _ in range(n)]
    
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    pollens = []
    for i in range(n):
        for j in range(n):
            burst = pollen = balloon[i][j]

            # 델타 제어(방향 전환)
            for k in range(4):

                # 길이 제어
                for l in range(1,burst+1):
                    if 0 <= i+di[k]*l < n and 0 <= j+dj[k]*l < n:
                        pollen += balloon[i+di[k]*l][j+dj[k]*l]
                    else: # 백트래킹
                        break                     
            pollens.append(pollen)

    print(f'#{tc} {max(pollens)-min(pollens)}')