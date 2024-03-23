def fibo(n):
    if n == 0:
        return 0
    
    # 기저 조건(종료 조건)
    if n == 1:
        return 1
        
    # 재귀 호출 : fibo(n) = fibo(n-1) + fibo(n-2)
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))

