t = int(input())

for tc in range(1,t+1):
    arr = list(map(int,input().split()))
    cnt = 0
    if arr[2] < 3 or arr[1] < 2:
        cnt = -1
    
    else:
        if arr[1] >= arr[2]:
            cnt += arr[1] - (arr[2] - 1)
            arr[1] = arr[2] - 1
        
        if arr[0] >= arr[1]:
            cnt += arr[0] - (arr[1] - 1)
    
    print(f'#{tc} {cnt}')