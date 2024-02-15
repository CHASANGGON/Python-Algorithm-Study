T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    pizza = input().split()
    pizza = [(i+1, int(pizza[i])) for i in range(M)] # 출력을 위해 인덱스 추가
    
    
    # 처음에 화덕의 개수 만큼 피자 넣기
    pot_pizza = pizza[:N]
    
    # 나머지
    rest_pizza = pizza[N:]
    
    #피자가 1개남을때까지 반복
    while len(pot_pizza) != 1:
        
        # 치즈가 있으니, 꺼내서 반 줄이고
        num, cheese = pot_pizza.pop(0)
        cheese //=2
        
        # 치즈가 남아있으면 제일 뒤로 보내고
        if cheese:
            pot_pizza.append((num, cheese))
        
        # 치즈가 없으면 새로운 피자 삽입
        else: 
            if rest_pizza:
                pot_pizza.append(rest_pizza.pop(0))
                # 어차피 피자가 빠진 위치에 넣으면 되니까 append
    
    # 화덕에 피자가 1개 남을 때까지 반복하니까 마지막에 pop해서 num을 출력하면 됨
    print(f'#{test_case} {pot_pizza.pop()[0]}')