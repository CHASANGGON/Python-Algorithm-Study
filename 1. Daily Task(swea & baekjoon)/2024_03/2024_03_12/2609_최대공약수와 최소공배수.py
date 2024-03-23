# 최대 공약수 구하기
def GCD(a,b):
    # 오른쪽의 수가 0일 때
    # 왼쪽의 수가 최대 공약수!
    if b == 0:
        return a
    # 오른쪽의 수가 0이 아니라면
    # 오른쪽의 수가 0이될 때까지 재귀 호출!
    return GCD(b,a%b)

import sys
input = sys.stdin.readline

a, b = map(int,input().split())

# 오른쪽의 수가 더 크다면 두 수를 교환
if a < b:
    a,b = b,a

# 최대 공약수 구하기
gcd = GCD(a,b)
print(gcd)

# 최소 공배수 * 최대 공약수 = 두 수의 곱
print(a*b//gcd)