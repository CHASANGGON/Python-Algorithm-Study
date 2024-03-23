# 1. make_set으로 먼저 자기 자신을 대표로 하는 집합을 만든다
# 2. 신청서를 참고하여 같은 집합으로 묶어주고, 대표자를 선정해준다
# 3. 모든 요소들에 대해서 find를 돌려서 부모를 똑바로 지정해준다.(효율적인 코드를 위해!)

def find(x):
    if x == parent[x]: # 대표자가 자기 자신과 일치하면
        return x #  바로 반환
    # 대표자가 자기 자신과 일치하지 않으면
    parent[x] = find(parent[x]) # 재귀 호출을 보내고 -> 돌아온 값을 자기 자신에게 갱신(효율적인 코드를 위해)
    return parent[x] # 그리고 새롭게 갱신한 값을 반환

def union(x,y):
    root_x = find(x) # 대표자 찾기(그래프로 생각하면 루트 노드)
    root_y = find(y) # 대표자 찾기

    # 제약 조건 : 큰 수를 대표자로 선정하기
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
        union(paper[i*2]-1, paper[i*2+1]-1) # 인덱스를 위해 -1씩 보정
    
    for x in range(n): # 모든 집합들을 대상으로 대표자 찾기 함수를 실행시켜줘야 갱신된다!
        find(x)
    
    result = len(list(set(parent))) # 세트 연산을 통해서 대표자만 남기기
    
    print(f'#{tc} {result}')