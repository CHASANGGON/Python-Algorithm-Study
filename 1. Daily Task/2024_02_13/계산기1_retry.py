T = 10

for test_case in range(1,T+1):
    input()
    formula = input()
    
    # 1. postfix로 변환
    stack = []
    postfix = ''
    for f in formula:
        
        # 1. 숫자
        if f.isdigit():
            postfix += f
            
        # 2. 연산자
        elif f == '+':            
            if stack:
                postfix += stack.pop()
                stack.append(f)
            else:
                stack.append(f)
    if stack:
        postfix += stack.pop()



    # 2. 후위 표기식을 계산            
    stack = []
    for p in postfix:
        
        # 1. 숫자
        if p.isdigit():
            stack.append(int(p))
        
        # 2. 연산자
        elif p == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
            
    print(f'#{test_case} {stack.pop()}')