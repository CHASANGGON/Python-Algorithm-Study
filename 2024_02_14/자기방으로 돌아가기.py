T = int(input())
for test_case in range(1,T+1):

    n = int(input())

    counting_lst = [0]*401 # 카운팅을 위한 리스트

    for i in range(n):
        start, end = map(int,input().split())

        start, end = min(start,end), max(start,end)  # 시작 위치가 더 작은 경우만 생각하려고(그게 편함)
        if start % 2 == 0: # 시작 위치가 짝수면, 홀수 위치도 못 씀
                           # 그림 잘 보면 이해 됨
                           # room2 에서 출발한다고 생각하면, room1도 못 지나감
            start -= 1
        if end % 2 == 1:   # 이것도 마찬가지
            end += 1
        
        for i in range(start,end+1): # 카운팅
            counting_lst[i] += 1
    
    print(f'#{test_case} {max(counting_lst)}') # max값이 정답!