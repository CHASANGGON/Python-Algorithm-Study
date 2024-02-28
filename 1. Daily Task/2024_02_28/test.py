def f(i,s):
    if i == 2:
        print(*p)

    else:
        for j in range(i,3):
            p[i], p[j] = p[j], p[i]
            f(i+1,s)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
n = 2
f(0,0)