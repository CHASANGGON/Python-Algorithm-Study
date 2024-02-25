N, P = map(int, input().split())

#0~6번 줄에 대해, 각 줄에서 눌러야 할 프렛 번호를 추가할 리스트 생성
line_lst = [[0] for _ in range(7)]

#멜로디를 연주하는데 필요한 최소 손가락 움직임 (결과값)
cnt = 0

for _ in range(N):
    l, p = map(int, input().split())

    #해당 줄의 더 높은 프렛을 이미 누르고 있는 경우 => 손가락을 하나씩 떼야함
    while line_lst[l][-1] > p:
        line_lst[l].pop()
        cnt += 1

    #이미 누르고 있는 줄의 프렛을 또 눌러야 하는 경우 => continue ~^^
    if line_lst[l][-1] == p:
        continue

    #그 외의 경우, 해당 줄에 눌러야 하는 프렛 번호 추가
    line_lst[l].append(p)
    cnt += 1

print(cnt)