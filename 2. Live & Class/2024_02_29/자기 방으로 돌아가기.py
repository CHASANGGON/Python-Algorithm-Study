t = int(input())

for tc in range(1,t+1):

    n = int(input())

    # 카운팅을 위한 리스트
    cnt_lst = [0]*401

    for _ in range(n):
        start, end = map(int,input().split())
        
        # 동시에 할당하지 않으면 값 하나가 삭제될 수 있음
        start, end = min(start,end), max(start,end)

        # 2번방에서 출발해도 1번방을 사용할 수 없다
        if start % 2 == 0:
            start -= 1
        
        # 3번방으로 가야해도 4번방을 사용할 수 없다
        if end % 2 == 1:
            end += 1
        
        # 카운팅
        for i in range(start,end+1):
            cnt_lst[i] += 1

    print(f'#{tc} {max(cnt_lst)}')