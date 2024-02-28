t = int(input())

for tc in range(1,t+1):

    n, m = map(int,input().split()) # n개의 화물 / m대의 트럭
    
    wi = list(map(int,input().split())) # 화물의 무게
    ti = list(map(int,input().split())) # 트럭의 적재용량

    wi.sort()
    ti.sort()

    s = 0

    # 각 화물을 하나씩 고려
    for w in wi[::-1]:
        if ti and w <= ti[-1]:
            ti.pop()
            s += w

    print(f'#{tc} {s}')