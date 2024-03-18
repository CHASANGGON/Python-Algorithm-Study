import sys
input = sys.stdin.readline

n = int(input())

people = list(map(int,input().split()))

# 오름차순으로 정렬 -> 그래야 바로 뒷 사람의 대기시간이 최소로 줄어듬
people.sort()

s = 0
for i in range(1,n+1):
    s += sum(people[:i])

print(s)