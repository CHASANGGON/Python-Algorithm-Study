def f(i):
    if i == n:
        print(*lst)
        return

    else:
        for j in range(1,6+1):
            lst.append(j)
            f(i+1)
            lst.pop()

lst = []
n = 3

f(0)