def fish_shaped_bun():
    for i in range(n):
        if (visitor[i]//m)*k < i+1:
            print(f'#{tc} Impossible')
            return
    print(f'#{tc} Possible')
t = int(input())

for tc in range(1,t+1):
    n, m, k = map(int,input().split())
    visitor = list(map(int,input().split()))
    visitor.sort()
    fish_shaped_bun()