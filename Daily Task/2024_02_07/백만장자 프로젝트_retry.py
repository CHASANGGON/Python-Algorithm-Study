T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    margin = 0
    while price:
        max_price = max(price)
        max_price_idx = price.index(max_price)
        margin += max_price*max_price_idx - sum(price[0:max_price_idx])
        price = price[max_price_idx+1:]
    print(f'#{tc} {margin}')