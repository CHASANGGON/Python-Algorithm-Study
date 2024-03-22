def find(x):
    if x == parent[x]: # 소년 가장
        return x # 자신(부모) 반환
    parent[x] = find(parent[x]) # 부모 찾아서 반납
    return parent[x]

def union(x, y):
    root_x = find(x) # 부모 찾아와!
    root_y = find(y) # 부모 찾아와!
    
    if root_x > root_y: # 누가 더 세노
        parent[root_y] = root_x # 더 센 사람이 부모해!
    else:
        parent[root_x] = root_y
    
t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    
	# 자기 자신을 부모로 하는 집합 생성(소년가장)
    parent = list(range(n))
    
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        union(x, y)

    for x in range(n): # 부모 값으로 모든 배열을 갱신
        find(x)
        
    print(f'#{tc} {len(list(set(parent)))}') # 부모의 수 = 그룹의 수