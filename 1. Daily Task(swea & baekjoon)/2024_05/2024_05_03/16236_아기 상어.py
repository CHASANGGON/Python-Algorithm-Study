import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# bfs를 매번 하는 것보다는
# 리스트나 딕셔너리에 모든 값들을 저장한 후에
# 꺼내서 좌표값의 차이를 이용해 값을 찾아가면 더 빠르지 않을까