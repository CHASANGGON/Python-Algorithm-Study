t = int(input())

for tc in range(1,t+1):
    n = int(input())

    prices = list(map(int,input().split()))

    margin = 0
    before_max = 0
    for price in prices[::-1]:
        if price > before_max:
            before_max = price
        elif price <= before_max:
            margin += before_max - price
    
    print(f'#{tc} {margin}')