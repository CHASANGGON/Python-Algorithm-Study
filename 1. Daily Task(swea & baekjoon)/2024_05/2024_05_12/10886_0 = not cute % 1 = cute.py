n = int(input())
one, zero = 0, 0
for _ in range(n):
    a = int(input())
    if a:
        one += 1
    else:
        zero += 1
if one > zero:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')