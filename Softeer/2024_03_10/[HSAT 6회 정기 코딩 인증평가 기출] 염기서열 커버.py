def wild_check(n):
    for i in range(m):
        for j in range(n):
            if arr[j][i] == '.':
                return i
    return -1


import sys
input = sys.stdin.readline

n, m = map(int,input().split())

arr = [input().rstrip() for _ in range(n)]

wild_check(n)

print(wild_check)

arr.sort()
for a in arr:
    print(a)

multiple = 1
total_max = 1

for i in range(m):
    
    sequence = []
    wild_card = False
    
    for j in range(n):
        if arr[j][i] == '.':
            wild_card = True
        
        
    # wild card가 있으면 최댓값만 갱신하고, 곱 x 
    if wild_card:
        total_max = max(total_max,len(list(set(sequence))))
    # wild card가 없으면 종류만큼 곱
    else:
        multiple *= len(list(set(sequence)))
        
print(total_max*multiple)