import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0

# 동전의 금액이 큰 순서부터 차례대로 비교 및 전체 금액에서 차감
for coin in coins[::-1]:
    while coin <= k:
        k -= coin
        cnt +=1
    if k == 0:
        print(cnt)
        break