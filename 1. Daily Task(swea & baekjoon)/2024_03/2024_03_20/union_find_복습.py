def make_set(x):
    parent[x] = x

def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    
    # 제약 조건 : 숫자가 큰 녀석을 부모로 설정
    if root_x > root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        
            
    
N = int(input()) # N개의 요소
parent = [0] * N # 대표를 저장할 리스트

for x in range(N):
    make_set(x)

union(0, 1) # 0과 1을 합치기 -> (0,1)부모는 1
union(3, 2) # 3과 2를 합치기 -> (2,3)부모는 3
union(0, 4) # 0과 4를 합치기 -> (0,1,4) 부모는 4
find_set(0)

# 4 4 3 3 4
print(f'부모 테이블 {parent}')