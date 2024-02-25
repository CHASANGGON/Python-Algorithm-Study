# 7명의 키의 합이 100
# 9명 난쟁이의 키가 주어짐 -> 7명을 찾기
# 9명 모두 키가 다름

# 여러 가지면 아무거나 출력 -> DFS 하다가 함수를 통해서 return 하면
# 최소 시간을 보장 가능할듯


# 그래서 그냥 간단하게 for문을 7개 겹쳐써도 되지만


# 반대로 9명의 합에서 2명을 빼는 2중 for문 구조로 푸는 게 훨씬 빠를 듯


# 9c2의 조합을 만들어도 되고, 단순하게 2중 for을 써도 됨
# 7명의 키의 합이 100
# 9명 난쟁이의 키가 주어짐 -> 7명을 찾기
# 9명 모두 키가 다름
# 여러 가지면 아무거나 출력 -> DFS 하다가 함수를 통해서 return 하면
# 최소 시간을 보장 가능할듯
# 그래서 그냥 간단하게 for문을 7개 겹쳐써도 되지만
# 반대로 9명의 합에서 2명을 빼는 2중 for문 구조로 푸는 게 훨씬 빠를 듯
# 9c2의 조합을 만들어도 되고, 단순하게 2중 for을 써도 됨
def f(s, dwarf):

    for i in range(9-1):
        for j in range(i+1,9):
            if s - dwarf[i] - dwarf[j] == 100:
                return [i,j]           

import sys
input = sys.stdin.readline

# 입력 받기
dwarf = [0]*9
for i in range(9):
    dwarf[i] = int(input())

# 후에 오름차순 출력을 위해 미리 정렬 
dwarf.sort()

# 함수 호출
faux_dwarf = f(sum(dwarf), dwarf)

# 리턴된 리스트를 참고하여 출력
for i in range(9):
    if i not in faux_dwarf:
        print(dwarf[i])