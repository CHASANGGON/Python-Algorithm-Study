# 테스트케이스 수 T
T = 10
for _ in range(1, T + 10):
    # 입력
    # 테스트케이스 번호 tc
    tc = int(input())
    password = list(map(int, input().split()))

    # 로직
    i = 1  # 감소시킬 값 (카운트 값)
    # 패스워드의 맨 뒤의 요소가 0이 될때까지 반복...!
    while password[-1] != 0:
        # 패스워드를 앞에서 하나의 값을 꺼내어 i씩 감소시키고
        x = password.pop(0)
        x = x - i
        # x가 0 이하가 된다면 0으로 만들어준다...!
        if x < 0:
            x = 0
        # 다시 뒤에 삽입! (그리고, i 는 1 증가)
        password.append(x)
        i = i + 1
        if i > 5:
            i = 1
    # 출력
    print(f"#{tc}", *password)