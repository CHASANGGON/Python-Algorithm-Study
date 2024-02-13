T = int(input())

for test_case in range(1,1+T):

    formula = input().split()

    stack = []
    print(f'#{test_case} ',end='')
    
    for f in formula:
        # 1. 숫자
        if f.isdigit():
            stack.append(int(f))

        # 2. 연산자
        elif f in '+-/*.': 
            if len(stack) >= 2 and f in '+-/*':
                # 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고
                b = stack.pop() # 순서 주의..... 이거 때문에 계속 틀렸어요..
                a = stack.pop()
                
                # 결과를 다시 스택에 넣는다.
                if f == '+':
                    stack.append(a + b)
                elif f == '-':
                    stack.append(a - b)
                elif f == '/':
                    stack.append(a // b)
                elif f == '*':
                    stack.append(a * b)
            
            elif len(stack) == 1 and f == '.': # '.'은 스택에서 숫자를 꺼내 출력한다.
                    print(stack.pop())
                    break
            else:
                print('error')
                break
            
        # 3. 잘못된 입력    
        else:
            print('error')
            break