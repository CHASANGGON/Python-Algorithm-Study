# make 과정 : 초기화, 나 자신을 부모로 갖는 단일 그룹 조성..!

def init(n):
    # 각 요소가 자기 자신을 부모로 갖는 일차원 배열을 반환
    parent = list(range(n)) # 0 ~ n-1
    return parent

# find : x에 속한 그룹의 대표(조상)을 찾아라
# 조상(대표자)은 자기 자신을 가리키고 있다...!
def find(x):
    # x가 대표자이므로 반환하는 기저조건
    if x == parent[x]:
        return x 
    
    # 재귀 호출을 통해서 부모를 계속 탐색(대표자 반환)
    parent[x] = find(parent[x])
    return parent[x]

# union : x와 y 두 그룹을 한 그룹으로 합쳐라
# - 각 대표자들을 찾고 합치기!!
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    # root_x의 부모를 
    # root_y로 설정하기
    # 제약 조건 : 요소의 번호가 더 작은 것을 대표자로 삼게 만드시오..!
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y



N = 5 # 요소의 개수
parent = init(N)

union(0, 1)
union(3, 2)
union(0, 4)

print(f'부모 테이블 {parent}')
print(find(1))
print(find(3))

