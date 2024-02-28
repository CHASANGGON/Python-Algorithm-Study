# 중간 위치에 설치했을 때가 최소합을 가진다
# 집에만 안테나를 설치할 수 있다고 했으니 중간 집에 설치하면 된다.
# 짝수 개면 비교를 하면 되고
# 홀수 개면 중간집을 고르면 된다.

def calc(num):
    s = 0
    for a in arr:
        s += abs(num-a)
    return s

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
arr.sort()

if n % 2 == 0:
    if arr[n//2] == arr[n//2-1]:
        print(arr[n//2])
    else:
        if calc(arr[n//2]) < calc(arr[n//2-1]):
            print(arr[n//2])
        else:
            print(arr[n//2-1])
else:
    print(arr[n//2])