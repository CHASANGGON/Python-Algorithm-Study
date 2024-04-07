import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort()
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, (n-i)*ropes[i])
print(max_weight)