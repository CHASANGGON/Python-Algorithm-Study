T = int(input())
for test_case in range(1, T+1):
    string = list(input())

    check = [] # 스택으로 사용할 리스트
    for s in string:
        if s == '}' and len(check) != 0 and check[-1] == '{': # 괄호의 짝이 맞으면 pop을 해서 check 리스트를 비워줌
            check.pop()
        elif s == ')' and len(check) != 0 and check[-1] == '(': 
            check.pop()


        elif s == '{' or  s == '(': # 좌측 괄호가 들어온다면 append 를 해서 check 리스트에 추가
            check.append(s)         # 우측 괄호가 들어온다면 제일 마지막에 append 된 값과 비교할 것이고, 이 때 좌측 괄호가 있어야 함
        elif s == '}' or s == ')': # 조건을 만족하지 않는 나머지를 append 해도 되고, 안 해도 됨
            check.append(s)

    # check 리스트(stack으로 사용)에 괄호의 짝이 맞으면 pop을 하였기 때문에
    # valid 한 괄호쌍이라면 최종값이 0이 남아야 함
    if len(check) != 0: 
        is_valid = 0
    else: is_valid = 1
    print(f'#{test_case} {is_valid}')