from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
arr = [arr for _ in range(k)]
pprint(arr)