t = int(input())

for tc in range(1,1+t):
    n = int(input())
    
    farm = [list(map(int,list(input()))) for _ in range(n)]
    
    profit = farm[n//2][n//2]
    farm[n//2][n//2] = -1
    q = [[n//2,n//2]]
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    
    for _ in range(n//2):
        next_q = []
        while q:
            i,j = q.pop()
            for k in range(4):
                if farm[i+di[k]][j+dj[k]] != -1:
                   profit += farm[i+di[k]][j+dj[k]]
                   farm[i+di[k]][j+dj[k]] = -1
                   next_q.append([i+di[k],j+dj[k]])
        q = next_q[:]

    print(f'#{tc} {profit}')