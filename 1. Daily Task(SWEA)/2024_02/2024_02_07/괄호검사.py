T = int(input())
for test_case in range(1, T+1):
    string = list(input())

    check = []
    
    is_valid = 1
    for s in string:
        if s == '}' and len(check) != 0 and check[-1] == '{': 
            check.pop()
        elif s == ')' and len(check) != 0 and check[-1] == '(': 
            check.pop()
        elif s == '{' or  s == '(':
            check.append(s)
        elif s == '}' or s == ')': # 조건을 만족하지 않는 나머지를 append 해야 아래의 if 문에서 걸러짐
            check.append(s)

    if len(check) != 0:
        is_valid = 0
    
    print(f'#{test_case} {is_valid}')