def subset(lst, m):
    
    max_s = 0
    max_lst = []
    for i in range(1<<m):
        subset = []
        for j in range(m):
            if i & (1<<j):
                subset.append(lst[j])
            if sum(subset) <= c:
                ss = 0
                for s in subset:
                    ss += s**2
                if ss > max_s:
                    max_s = ss
                    max_lst = subset
    return max_lst


def calc(lst):
    max_lst = subset(lst, m)

    for i in range(len(max_lst)):
        max_lst[i] = max_lst[i]**2

    return sum(max_lst)

t = int(input())

for tc in range(1,t+1):

    n, m, c = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n-m+1):
            arr[i][j] = calc(arr[i][j:j+m])
    
    
    # 일꾼은 두 명
    result = 0
    for _ in range(2):
        max_honey = 0
        max_i, max_j = 0, 0
        for i in range(n):
            for j in range(n-1):
                if arr[i][j] > max_honey:
                    max_honey = arr[i][j]
                    max_i, max_j = i, j

        result += max_honey
        arr[max_i][max_j] = 0
        for i in range(1,m):
            if max_j - i >= 0:
                arr[max_i][max_j-i] = 0
        for i in range(1,m):
            arr[max_i][max_j+i] = 0

    print(f'#{tc} {result}')

    # podo seven zero!!