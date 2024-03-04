def find_prime(n):
    sieve = [True]*(n+1)

    m = int(n**0.5)
    for i in range(1,m):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

import sys
input = sys.stdin.readline

n = int(input())
lst = find_prime(n)
print(lst)
# 소수는 해당 수의 제곱근까지 구하면 된다
