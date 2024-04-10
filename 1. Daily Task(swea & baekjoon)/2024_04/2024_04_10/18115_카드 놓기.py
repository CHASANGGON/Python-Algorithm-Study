from collections import deque
import sys
input = sys.stdin.readline

# 제일 위의 카드 1장을 바닥에 내려놓는다.
# 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때
# 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때

# 입력
n = int(input())
skills = list(map(int, input().split()))

# 놓여 있는 카드들을 확인했더니 위에서부터 순서대로 1, 2, …, N
# 왼쪽이 젤 아래 / 오른쪽이 젤 위
cards = list(range(n,0,-1)) # 현재 카드

# 초기 카드 상태를 나타낼 변수
# 왼쪽이 젤 아래 / 오른쪽이 젤 위
origin = deque() 

for skill in skills[::-1]: # 스킬 반전 시키기
    if skill == 1: # 젤 위에서 뽑은 경우
        origin.append(cards.pop()) # 그러니 제일 오른쪽으로 append
    
    if skill == 2: # 위에서 두 번째 카드를 뽑은 경우
        temp = origin.pop() # 제일 위에 카드를 잠시 빼서 임시 변수 temp에 저장한 다음
        origin.append(cards.pop()) # 제일 위에 append한 다음
        origin.append(temp) # 임시 변수에 저장해둔 card를 append

    if skill == 3: # 제일 아래에서 뽑은 경우
        origin.appendleft(cards.pop()) # 제일 아래에 push(append left) -> 이거 때문에 deque을 사용해야함

# 순서가 다르므로 반전시켜서 출력해야함
# 덱은 반전이 안 되므로 리스트로 변환 시킨후
# 리스트 슬라이싱으로 반전시킨후
# 괄호제거를 위해 * 로 출력
print(*list(origin)[::-1])