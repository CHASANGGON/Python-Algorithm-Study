import sys
input = sys.stdin.readline

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    
    price = list(map(int,input().split()))
    
    margin = 0
    max_price = 0
    for p in price[::-1]:
        if p > max_price:
            max_price = p
        else:
            margin += max_price - p
            
    print(margin)