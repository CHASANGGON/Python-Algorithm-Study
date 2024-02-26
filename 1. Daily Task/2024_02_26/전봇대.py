t = int(input())

for tc in range(1,t+1):
    n = int(input())

    lst = []
    cnt = 0

    for _ in range(n):
        a, b = map(int,input().split())
        lst.append([a,b])

        for l in lst:
            if (l[0] < a and l[1] > b) or (l[0] > a and l[1] < b):
                cnt += 1

    print(f'#{tc} {cnt}')