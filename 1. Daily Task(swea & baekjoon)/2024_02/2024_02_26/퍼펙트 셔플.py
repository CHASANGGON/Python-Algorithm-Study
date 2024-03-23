t = int(input())

for tc in range(1,t+1):
    n = int(input())

    cards = input().split()
    new_cards = []
    i = 0
    l, r = 0, n//2
    if n % 2:
        r += 1
    while i < n:
        if i % 2:
            new_cards.append(cards[r])
            r += 1
        else:
            new_cards.append(cards[l])
            l += 1
        i += 1
    
    print(f'#{tc} ',end='')
    print(*new_cards)