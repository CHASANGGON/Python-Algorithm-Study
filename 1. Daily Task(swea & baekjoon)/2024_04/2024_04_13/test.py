N, K = map(int, input().split())
n = 1
while n < N:
    n *= 2
for i in range(K):
    while n > N:
        n //= 2
    N -= n
    if N == 0:
        print(0)
        break
else:
    print(n-N)