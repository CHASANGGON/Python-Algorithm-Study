t = int(input())

for tc in range(1,t+1):
    n = int(input())

    lst = input().split()

    print(f'#{tc}',end=' ')

    # 홀수
    if n % 2:
        for i in range(n//2+1):
            print(lst[i],end=' ')
            if i+n//2+1 < n:
                print(lst[i+n//2+1],end=' ')


    # 짝수
    else:
        for i in range(n//2):
            print(lst[i],end=' ')
            print(lst[i+n//2],end=' ')
    
    print()