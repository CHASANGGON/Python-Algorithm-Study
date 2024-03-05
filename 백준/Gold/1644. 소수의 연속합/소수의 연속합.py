def find_prime(n):
    sieve = [True]*(n+1)

    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]

import sys
input = sys.stdin.readline

n = int(input())
prime_lst = find_prime(n)

l = len(prime_lst)
i, j = 0, 1
cnt = 0
while i < l and j < l+1:
    if sum(prime_lst[i:j]) < n:
        j += 1
    elif sum(prime_lst[i:j]) > n:
        i += 1
    else:
        cnt += 1
        i += 1
        j += 1

print(cnt)