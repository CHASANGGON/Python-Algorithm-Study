T = 10
for test_case in range(1,T+1):
    input()
    password = list(map(int,input().split()))
    subtract_value = (min(password)//15-1)*15   
    # 뺄 값은 1~5(1 cycle) 다섯 자리, 암호는 8자리
    # -> 40번마다(8 cycle) 각 자리가 15씩 감소
    # password의 "(최솟값을 15로 나눈 몫보다 1 작은 값) * 15" 를 빼주기
    # "1 작은 값"인 이유 -> 나누어 떨어지는 경우 바로 0이 발생
    # 0이 발생한 경우 바로 순차적으로 실행되는 코드라면 진작 종료되었어야 하지만
    # 이 코드는 임의로 15씩 빼준 것이기 때문에 password의 젤 뒤가 아닌 곳에 0이 존재할 수 있다.
    # 그래서 1 작은 값만큼 빼준다음 cycle을 돌려서 password를 찾으면 수월하다.
    for i in range(8):
        password[i] -= subtract_value

    i = 1
    while 0 not in password: # 0이 발생할 때 까지 실행
        new_value = password.pop(0) - i
        if new_value <= 0: # 0보다 작아지는 경우
            password.append(0) # 0으로 유지되며, 프로그램은 종료
        else: 
            password.append(new_value) # 감소한 뒤 맨 뒤로
        i = i%5 + 1 # i = 1 ~ 5

    print(f'#{test_case} ',end='')
    print(*password)