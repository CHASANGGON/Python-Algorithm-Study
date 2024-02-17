T = 10

# 중위식 -> 후위식 -> 계산
for test_case in range(1,T+1):
    input()
    formula = input()
    
    # 1. 중위식 -> 후위식
    isp = {'(':0, '+':1, '-':1, '*':2, '/':2, ')':0} # 스택 우선순위
    icp = {'(':3, '+':1, '-':1, '*':2, '/':2, ')':0} # 입력 우선순위
    
    stack = []
    postfix = ''
    for f in formula:
        # 1. 숫자
        if f.isdigit():
            postfix += f
           
        # 2. 연산자    
        elif f in icp:
            
            # 1. stack top보다 우선순위가 높을 때
            if stack and icp[f] > isp[stack[-1]]:
                stack.append(f)
                
            # 2. stack top보다 우선순위가 높지 않을 때
            elif stack and icp[f] <= isp[stack[-1]]:
                while stack and icp[f] <= isp[stack[-1]]:
                    p = stack.pop()
                    if p != '(':
                        postfix += p
                if f != ')':stack.append(f)   
                     
            # 3. stack이 비어있을 때        
            else:
                stack.append(f)
    while stack:
        postfix += stack.pop()
        
        
    # 2. 후위식 -> 계산
    stack = []
    for p in postfix:
        if p.isdigit():
            stack.append(int(p))
        else:
            b = stack.pop()
            a = stack.pop()
            if p == '+':
                stack.append(a+b)
            if p == '-':
                stack.append(a-b)
            if p == '*':
                stack.append(a*b)
            if p == '/':
                stack.append(a//b)
    print(f'#{test_case} {stack[-1]}')