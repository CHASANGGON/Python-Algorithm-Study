memo = [0] * 15
def fibo(n):
    if memo[n] != 0:
        return memo[n]
    
    # 기저 조건(종료 조건)
    if n < 2:
        return n
    
    # 재귀 호출 : fibo(n) = fibo(n-1) + fibo(n-2)
    # 연산한 결과값을 배열에 저장하고, 재사용하겠다!
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())
print(fibo(15))

