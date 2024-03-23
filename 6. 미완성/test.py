origin_d = 315
for offset_d in range(1,5): # 반시계 방향으로 90도 회전
    d = (origin_d - offset_d) % 4
    print(d)