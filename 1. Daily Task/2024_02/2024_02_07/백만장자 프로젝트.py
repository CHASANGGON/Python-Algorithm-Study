T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    price = list(map(int,input().split()))

    # price 리스트의 최댓값을 구한후, 앞에서부터 접근하며 최댓값인 가격과 현재 인덱스에 해당하는 가격의 차이를 누적합하고,
    # 최댓값 이후에서 새로운 최댓값을 구한후, 새로운 최댓값 가격과의 차이를 누적합하는 방식으로 해보았으나 시간초과가 발생함
    # 이렇게 하면 max연산 & sum연산 & 또한 해당 max값의 index를 찾는 연산 & 또한 언제 끝날지 모르기에 while문을 통한 조건 연산
    # 연산이 매우 많아져서 시간을 초과한다.

    # 그래서 거꾸로 뒤에서부터 접근하는 방식을 생각해보았음
    # 제일 끝 요소를 최댓값으로 저장한 후에 인덱스를 줄여나가면서, 만약 해당 값이 기존의 최댓값보다 작다면, 
    # 그 차이만큼 margin 이 발생하므로 누적합하고, 새로운 최댓값이 발생한다면, 최댓값을 갱신하면 된다.
    # 이렇게 하면 for 연산 & if 연산 & 합 연산 이므로 계산량이 획기적으로 줄어들게 되니까 시간초과를 해결할 수 있다.
    # 또한, 이렇게 하면 현재 값이 기존의 최댓값보다 작아야지만 누적합을 시행하므로 절대로 margin이 음수가 될 일이 없다.
    
    max_price = price[-1]
    margin = 0

    for p in price[::-1]:
        if p > max_price:
            max_price = p
        else:
            margin += max_price - p

    print(f'#{test_case} {margin}')