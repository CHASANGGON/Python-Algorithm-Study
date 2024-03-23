# 문제에서 설명하는 "번갈아"의 의미를 이해하려면 "번갈아가 아닌 경우"를 생각해야 한다.
# "오른쪽-오른쪽" 같은 경우가 "번갈아가 아닌 경우"다

# 그러니까 
# 1. 처음 찾는 경우는 "번갈아가 아닌 경우"가 아니기 때문에 카운트해주면 된다.
# 2. 오른쪽 또는 왼쪽으로 한 번만 간 경우도 "번갈아가 아닌 경우"가 아니기 때문에 카운트해주면 된다.

def bs(low, high, target, before):
    if low <= high:
        mid = (low+high)//2

        # 바로 찾는 경우    
        if target == n_lst[mid]:
            return True
                
        if target < n_lst[mid]:
            if before == 'l':
                return False
            else:
                return bs(low, mid - 1, target, 'l')
        else:
            if before == 'r':
                return False
            else:
                return bs(mid + 1, high, target, 'r')
    
    # 찾는 값이 없을 때
    else:
        return False

t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    n_lst.sort()
    m_lst = list(map(int, input().split()))
    
    cnt = 0
    
    for m in m_lst:
        if bs(0, N-1, m, ''):
            cnt += 1
    
    print(f'#{tc} {cnt}')