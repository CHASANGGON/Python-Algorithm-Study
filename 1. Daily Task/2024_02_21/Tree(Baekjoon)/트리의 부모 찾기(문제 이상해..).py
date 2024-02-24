import sys
input = sys.stdin.readline

n = int(input())
vertex = [[] for _ in range(n+1)]

# 무방향으로 만든 다음에, 루트에서 출발해서 방향을 제거
for _ in range(n-1):
    s, e = map(int,input().split())
    vertex[s].append(e)
    vertex[e].append(s)

parent = [0]*(n+1)
stack = []
for d in vertex[1]:
    stack.append([1,d]) # 부모 자식

while stack:
    p, d = stack.pop()
    if parent[d] == 0: # 부모 없으면
        parent[d] = p # 니가 해라
    for a in vertex[d]:
        if parent[a] == 0:
            stack.append([d, a])
    
for i in range(2,n+1):
    print(parent[i])