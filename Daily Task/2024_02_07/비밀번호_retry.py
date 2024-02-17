# 스택을 사용한 풀이
T = 10
for test_case in range(1,T+1):
    n, password = input().split()
    decrypted_password = [] # 스택으로 사용할 리스트 -> 최종 비밀번호에 해당

    for p in password:
        if len(decrypted_password) == 0: # 스택이 비었다면 일단 push(append)
            decrypted_password.append(p)
        elif p == decrypted_password[-1]: # 스택의 가장 최근에 push된 값과 현재의 값이 일치한다면
            decrypted_password.pop()      # 이어붙여진 두 문자(숫자)가 일치하는 상황 -> pop
        else:       
            decrypted_password.append(p)  # else case 라면 이어붙여진 두 문자가 일치하지 않는 상황 -> push(append)
    print(f'#{test_case} ',end ='')
    print(*decrypted_password,sep='') # 리스트를 출력 형식을 맞추기 위해 unpacking 연산자