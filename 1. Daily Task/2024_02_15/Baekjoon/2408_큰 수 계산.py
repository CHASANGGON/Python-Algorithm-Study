# eval 함수
# 문자열로 식을 입력하면
# 해당식을 실행한 결과값을 반환하는 함수
# print(eval("3*5")) 이렇게 실행하면
# 15를 출력한다.

if __name__ == '__main__':
    equation = ''
    n = int(input())
    for _ in range(n + n - 1):
        equation += input()
    equation = equation.replace('/', '//')
    print(eval(equation))