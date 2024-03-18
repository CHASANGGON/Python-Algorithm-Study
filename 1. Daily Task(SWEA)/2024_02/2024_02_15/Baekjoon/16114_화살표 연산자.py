import sys
input = sys.stdin.readline

x, n = map(int,input().rstrip().split())
if n == 0 or (x < 0 and n == 1):
    print('INFINITE')
elif n % 2 == 1:
    print('ERROR')
elif x >= 0 and n == 1:
    print('0')
else:
    n = n // 2
    print((x + n - 1) // n - 1)