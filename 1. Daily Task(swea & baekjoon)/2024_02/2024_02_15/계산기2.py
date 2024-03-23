T = 10
for test_case in range(1,T+1):
    input()
    infix = input()
    # infix = '3+4+5*6+7'
        
        
    # 1. infix -> postfix 로 변환
    icp = {'*':2, '+':1} # in coming precedence
    isp = {'*':2, '+':1} # in stack precedence 
                         # * 연산자는 + 연산자와는 다르게 이어붙여서 실행이 가능하므로 isp 값은 1이다
                         # -> 그래야만 stack에 *가 누적되었다가, 한 번에 출력 가능
                         # -> *가 들어있는 상태에서, 우선순위가 동일한 + 가 입력되면 pop)
        

    stack = []
    postfix = ''
    for i in infix:
            
        if i.isdigit(): # 숫자는 바로 표기
            postfix += i
                
        elif not stack: # 스택이 비워져있다면 일단은 push
            stack.append(i)
                
        elif icp[i] > isp[stack[-1]]: # top원소의 우선 순위보다 높으면 push
            stack.append(i)
        else:
            while stack and icp[i] <= isp[stack[-1]]:
                postfix += stack.pop()
            stack.append(i)
    while stack:
        postfix += stack.pop()
    
    # 2. postfix 계산
    cal_stack = []
        
    for p in postfix:
        if p.isdigit():
            cal_stack.append(p)
        else:
            b = int(cal_stack.pop())
            a = int(cal_stack.pop())
                
            if p == '*':
                cal_stack.append(a*b)
            else:
                cal_stack.append(a+b)
                
    print(f'#{test_case} {cal_stack[-1]}')