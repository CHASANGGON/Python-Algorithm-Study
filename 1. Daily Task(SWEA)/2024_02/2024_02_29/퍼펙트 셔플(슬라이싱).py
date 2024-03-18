t = int(input())

for tc in range(1,t+1):
    n = int(input())

    lst = list(input().split())

    # 홀수
    if n % 2:
        l = lst[:n//2+1]
        r = lst[n//2+1:]

    # 짝수
    else:
        l = lst[:n//2]
        r = lst[n//2:]

    result = []
    while l or r:
        if l:
            result.append(l[0])
            l.pop(0)
        if r:
            result.append(r[0])
            r.pop(0)

    print(f'#{tc} ',end='')
    print(*result)