T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    cards = list(input().split())

    if n % 2 == 1:
        cards_left = cards[:n//2+1]
        cards_right = cards[n//2+1:]
    else:
        cards_left = cards[:n//2]
        cards_right = cards[n//2:]
    
    print(f'#{test_case} ',end='')
    while cards_left:
        print(cards_left.pop(0),end=' ')
        if cards_right:
            print(cards_right.pop(0),end=' ')
    print()