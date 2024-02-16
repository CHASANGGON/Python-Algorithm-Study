T = int(input())

for test_case in range(1,1+T):
    N, M = map(int,input().split()) # 가로 세로
    
    national_flag = [input() for _ in range(N)]
    # print(national_flag)

    total = 0
    cnt_lst = []
    for n in national_flag:
        cnt_lst.append([M-national_flag.count('W'),M-national_flag.count('B'),M-national_flag.count('R')]) 
    
    total += min(cnt_lst[0])+min(cnt_lst[-1])