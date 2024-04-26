from pprint import pprint
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split()) # 인벤토리에는 B개의 블록이 들어 있다
arr = [list(map(int, input().split())) for _ in range(n)]

# 인벤토리에 블록이 있으면, 채우기가 가능
# 인벤토리에 블록이 없으면, 제일 높은 칸에서 제일 낮은 칸으로 옮기면 됨
if b:
    for i in range(n):
        for j in range(m):
            pass