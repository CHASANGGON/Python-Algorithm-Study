t = int(input())

for tc in range(1,t+1):
    n = int(input())

    if n == (round(n**(1/3)))**3:
        print(f'#{tc} {round(n**(1/3))}')
    else:
        print(f'#{tc} {-1}')