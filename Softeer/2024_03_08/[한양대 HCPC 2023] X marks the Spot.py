import sys
input = sys.stdin.readline

n = int(input())
lst = [0]*n

for i in range(n):
    # 입력 받기
    a, b = input().split()
    # 길이 만큼 순회하면서
    for j in range(len(a)):
        # x or X 찾기
        if a[j] == 'x' or a[j] == 'X':
            # 해당 인덱스 값으로 b에 접근해서
            # 숫자 검사
            if b[j].isdigit():
                # 숫자는 바로 대입
                lst[i] = b[j]
            else:
                # 소문자는 대문자로
                lst[i] = (b[j].upper())
                
# join을 이용해서 이어붙여서 출력(내부값이 str타입이라서 가능)
print(''.join(lst))