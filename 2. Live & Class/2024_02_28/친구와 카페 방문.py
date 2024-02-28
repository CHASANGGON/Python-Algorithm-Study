# 둘 이상일 때의 경우의 수
# 기존의 비트 연산(모든 부분집합을 구하는 것)
# & if & len함수를 활용해서 부분집합의 요소의 개수 체크
# 기저 조건에서 개수 체크
# 2개 이상이면 최종 리스트에 append or 출력


friend = ['a','b,','c','d','e']
n = len(friend)

total_f = []
for i in range(1<<n):
    f = []
    for j in range(n):
        if i & (1<<j):
            f.append(friend[j])
    if len(f) >= 2:
        # print(f)
        total_f.append(f)

for f in total_f:
    print(f)

print(f'{len(total_f)}가지')