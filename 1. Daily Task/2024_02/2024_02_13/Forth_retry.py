# 숫자는 스택에 넣는다
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# .은 스택에서 숫자를 꺼내 출력한다.
# 형식이 잘못 됐으면 error

T = int(input())

for test_case in range(1,T+1):
    formula = input().split()
    
    stack = []
    print(f'#{test_case} ',end='')
    for f in formula:
        
        # 1. 숫자
        if f.isdigit():
            stack.append(int(f))
        
        # 2. 연산자
        elif f in '+-*/':
            # pop할 숫자가 두 개 있어야 정상 
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()

                # 연산자에 맞게 처리
                if f == '+':
                    stack.append(a+b)
                elif f == '-':
                    stack.append(a-b)
                elif f == '*':
                    stack.append(a*b)
                else:
                    stack.append(a//b)
                
            else:
                print('error')
                break
        
        # 3. 종료 ( . )
        else:
            # 스택에 1개만 남아있어야 정상
            if len(stack) == 1:
                print(stack.pop())
            else:
                print('error')
                break