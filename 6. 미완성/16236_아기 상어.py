import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
# 1. find shark (9)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            s_i, s_j = i, j # shark's i and j
            size = 1
            ate = 0
            break            

while True:        
    # 2. find fish that are smaller or the same size as shark size
    fish = [[] for _ in range(2*n-1)]
    can_eat = 0
    for i in range(n):
        for j in range(n):
            if 1 <= arr[i][j] <= size:
                fish[abs(s_i-i) + abs(s_j-j)].append((i,j))
                can_eat += 1
    

    # Termination condition : If the shark doesn't find the fish, it's over
    if can_eat == 0:
        print(ans)
        break

    for i in range(1,2*n-1):
        if fish[i]:
            fish[i].sort(key=lambda x : (x[1], x[0]))
            f_i = fish[i][0][0]
            f_j = fish[i][0][1]
            break
    
    # accumulated sum of output variable
    ans += abs(s_i-f_i) + abs(s_j-f_j)
    
    # update shark's position
    s_i = f_i
    s_j = f_j
    
    # The fish was eaten :)
    arr[s_i][s_j] = 0
    
    # size update
    ate += 1
    if ate == size:
        size += 1
        ate = 0

# 아 ** 지나가는 경로도 생각해야함..!