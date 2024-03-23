# 카운팅 정렬을 통해서 숫자를 파악한 후
# triplet 체크는 값이 3인지를 체크하면 되고,
# run 체크는 값 1이상이 연속한지를 보면 된다.
# 이 때 인덱스 에러 방지를 위해 끝에 2개를 더 붙여준다

t = int(input())

for tc in range(1,t+1):
    card = input().strip()

    # 카운팅
    cnt_lst = [0]*12 # 인덱스 에러를 피하기 위해 2개 더
    for c in card:
        cnt_lst[int(c)] += 1
    
    # 체크
    r_or_t = 0
    for i in range(10):
        while cnt_lst[i] >= 3:
            cnt_lst[i] -= 3
            r_or_t += 1
        while cnt_lst[i] and cnt_lst[i+1] and cnt_lst[i+2]:
            cnt_lst[i] -= 1
            cnt_lst[i+1] -= 1
            cnt_lst[i+2] -= 1
            r_or_t += 1
    
    if r_or_t == 2:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')