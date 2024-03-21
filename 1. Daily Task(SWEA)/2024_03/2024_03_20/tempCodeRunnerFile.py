# 1. make_set으로 먼저 자기 자신을 대표로 하는 집합을 만든다
# 2. 신청서를 참고하여 같은 집합으로 묶어주고, 대표자를 선정해준다
# 3. 모든 요소들에 대해서 find를 돌려서 부모를 똑바로 지정해준다.(효율적인 코드를 위해!)

def find(x):
    if x == parent[x]:
        return x    
    parent[x] = find(x)
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    # 제약 조건 : 큰 수를 대표자로 선정
    if root_x > root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

t = int(input())

for tc in range(1,t+1):
    
    n, m = map(int, input().split())
    paper = list(map(int, input().split()))
    
    # 함수대신 list & range로 바로 생성
    # 자기 자신을 부모로 갖는다
    parent = list(range(n))
    
    for i in range(m):
        union(paper[i*2]-1, paper[i*2+1]-1)
    
    for x in range(n):
        find(x)
    
    result = len(list(set(parent)))
    
    print(f'#{tc} {result}')