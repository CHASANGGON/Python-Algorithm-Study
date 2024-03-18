T = 10

for test_case in range(1,T+1):
    n = int(input()) # 찾아야 할 길이 입력 받기

    # 입력 받기
    key_board = [list(input()) for _ in range(8)] 

    cnt = 0
    for i in range(8): # 가로 방향 확인
        for j in range(8-n+1):
            is_palindrome = key_board[i][j:j+n] # 매 위치에서 해당하는 길이만큼 저장
            if is_palindrome == is_palindrome[::-1]: # 매번 회문인지 검사(반전시켜서)
                cnt += 1

    
    for i in range(8): # 세로 방향 확인
        for j in range(8-n+1): # n=4 -> range(5) : 0~4
            is_palindrome = ''
            for k in range(n):
                is_palindrome += key_board[j+k][i] # 세로 방향 문자열 생성
            if is_palindrome == is_palindrome[::-1]: # 매번 회문인지 검사
                cnt += 1

    print(f'#{test_case} {cnt}')

# 길이가 정해지지 않은 회문을 찾아야 했다면
# 매 위치에서 매번, 가능한 모든 길이의 회문을 고려해야하지만
# 친절하게도 찾아야 하는 회문의 길이가 주어진다.

# 그래서 매 위치([i][j])에서 매번(if), 해당하는 길이만큼만([j:j+n]) 고려해주면 된다.
# 리스트 인덱싱을 활용해서 [::-1] 을 한다면 쉽게 리스트를 반전시킬 수 있고
# 주어진 길이만큼만 검사하면 되니까, 주어진 길이가 n이라면
# 해당 길이의 리스트를 변수에 저장하고, a = [j:j+n]
# 리스트 슬라이싱으로 반전시켜서 비교해주면 된다.
# if a == a[::-1]
    