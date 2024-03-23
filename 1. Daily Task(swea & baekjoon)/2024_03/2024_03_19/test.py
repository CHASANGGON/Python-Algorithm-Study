def dfs(now, charge):
    global min_charge
    if now == n - 1:
        min_charge = min(min_charge, charge)
        return
    
    for j in range(1, 1 + battery[now]):
        if now + j <= n - 1:
            dfs(now + j, charge + 1)

t = int(input())
 
for tc in range(1,t+1):
     
    a = list(map(int,input().split()))
     
    n, battery = a[0], a[1:]

    min_charge = 99999    
    dfs(0, -1)
    
    print(f'#{tc} {min_charge}')