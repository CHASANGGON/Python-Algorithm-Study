def backtrack(i, now_charge):
    global min_charge
    
    # backtrack
    if now_charge >= min_charge:
        return
    
    if i >= 12:
        min_charge = min(min_charge, now_charge)
        return    
    
    backtrack(i+1, now_charge + charge[0]*days_of_use[i]) # 1일 이용권
    backtrack(i+1, now_charge + charge[1]*min(1,days_of_use[i])) # 1달 이용권 
    month_3 = False
    for j in range(i,i+3):
        if j < 12 and days_of_use[j]:
            month_3 = True
            break
    if month_3:
        backtrack(j+3, now_charge + charge[2]) # 3달 이용권
    else:
        backtrack(j+3, now_charge)


t = int(input())

for tc in range(1,t+1):
    charge = list(map(int, input().split())) # 1일, 1달, 3달, 1년
    days_of_use = list(map(int, input().split()))
    
    min_charge = charge[3]
    
    backtrack(0, 0)
    
    print(f'#{min_charge} ')