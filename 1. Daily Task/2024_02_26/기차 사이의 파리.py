t = int(input())
for tc in range(1,t+1):
    d, a, b, f = map(int,input().split())
    print(f'#{tc} {(d/(a+b))*f}')