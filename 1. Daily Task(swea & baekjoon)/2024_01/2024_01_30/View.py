for test_case in range(1, 11):
    n = int(input())
    h = [0,0] + list(map(int, input().split())) + [0,0]
    how_many = 0
    
    print(f'#{test_case} ',end='')
    
    for i in range(2,2+n):
        can_see = 0

        # 현재 빌딩 높이 - 좌우로 2칸까지의 빌딩 높이
        left_h = h[i] - h[i-1]
        left_left_h = h[i] - h[i-2]
        right_h = h[i] - h[i+1]
        right_right_h = h[i] - h[i+2]   

        # 이 중에서 최솟값이 조망권
        can_see = min(left_h,left_left_h,right_h,right_right_h)
        
        if can_see > 0: # I'm happy
             how_many += can_see
    print(how_many)