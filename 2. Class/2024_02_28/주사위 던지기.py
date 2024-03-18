def f(i):
    if i == n:
        print(p[:n])

    else:
        for j in range(i,6):
            p[i], p[j] = p[j], p[i]
            f(i+1)
            p[i], p[j] = p[j], p[i]

n = 3 # 몇 개의 주사위를 던질 것인지 -> 눈금의 개수 결정
p = list(range(1,7))

f(0)