import sys
imput = sys.stdin.readline

n = int(input())

a = [0]*41
a[0] = 1
a[1] =2

if n > 2:
    for i in range(2,n):
        a[i] = a[i-1] + a[i-2]
    b = n - 2
else:
    a = 1
    b = 0

print(a[n-2], b)