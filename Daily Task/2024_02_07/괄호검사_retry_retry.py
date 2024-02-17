T = int(input())
for test_case in range(1,T+1):
    string = input()
   
    stack = []
    for s in string:
        if s in '{(':
            stack.append(s)
        elif s in '})':
            if s == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif s == ')' and stack and stack[-1] == '(':
                stack.pop()

            # 필요한 이유 -> (})
            else:
                stack.append(s) 
        
    if stack:
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {1}')