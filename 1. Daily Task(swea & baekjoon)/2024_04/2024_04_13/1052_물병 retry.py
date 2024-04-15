import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 입력
num = 67108864 # n은 최대 10의 7승 -> 2의 26승 = 67,108,864 = 합쳐서 만들 수 있는 최대 크기의 물병

for _ in range(k): # k번 안에 모두 합칠 수 있는지? -> 합치지 못하면 그만큼 물을 사야한다
    # 남아 있는 n보다 작은 수 중에서 제일 큰 2의 n승 만들기(그리디)
    #   n보다 큰 수만큼의 물병을 만드려면 물을 사야하고, 
    #   n보다 작은 수는 있는 것들로 합쳐서 만들 수 있다
    while num > n:
        num //= 2
    n -= num

    if n == 0: # k번 안에 모두 합치면 사올 필요 없음
        print(0)
        break
if n: # k번 안에 합치지 못 해서 남아 있다면, 가장 가까운 2의 n승이 될 만큼 사오면 된다
    print(num-n)