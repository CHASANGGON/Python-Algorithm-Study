T = int(input())
 
for test_case in range(1, T + 1):
    input()
    nums = input()
    cards = [0]*10
    for num in nums:
        cards[int(num)] += 1

    max_card_count = max(cards)

    cards = cards[::-1]
    max_card_index = cards.index(max_card_count)

    print(f'#{test_case} {9-cards.index(max_card_count)} {max_card_count}')